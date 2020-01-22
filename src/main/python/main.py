import sys
from typing import Optional

import test_pb2 as proto
import socket
import queue
from google.protobuf.internal.decoder import _DecodeVarint32
class SockQueue(queue.Queue):

    def __init__(self, sock:socket) -> None:
        self.sock=sock
        super().__init__()

    def get(self):
        while self.empty():
            buf=self.sock.recv(1024)
            for b in buf:
                self.put(bytes([b]))
        return super().get()


def EncodeVarint(msg):
    value = len(msg)
    bits = value & 0x7f
    value >>= 7
    header_array = []
    while value:
        header_array.append(0x80 | bits)
        bits = value & 0x7f
        value >>= 7
    header_array.append(bits)
    re = bytes(header_array)
    return re


people = proto.People()
people.name = "asd"
people.id = 233

msg = people.SerializeToString()
msg_len = EncodeVarint(msg)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(("127.0.0.1", 8080))
tcp.send(msg_len)
tcp.send(msg)

lenBytes = b""
pos = 0
q = SockQueue(tcp)

while True:
    lenBytes += q.get()
    if (lenBytes[pos] & 0x80) != 0x80:
        break
    pos += 1
recv_len,new_pos= _DecodeVarint32(lenBytes, 0)
buf = b''
for i in range(recv_len):
    buf+=q.get()
recv_people= proto.People()
recv_people.ParseFromString(buf)
print(recv_people)


