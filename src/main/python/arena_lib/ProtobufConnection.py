import socket
from queue import Queue
from typing import Callable

import betterproto
from google.protobuf.internal.decoder import _DecodeVarint32


class SockQueue(Queue):

    def __init__(self, sock: socket) -> None:
        self.sock = sock
        super().__init__()

    def get(self):
        while self.empty():
            buf = self.sock.recv(1024)
            for b in buf:
                self.put(bytes([b]))
        return super().get()


class ProtobufConnection:
    def _encodeVarint(self, msg):
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

    def __init__(self, address_port: (str, int)) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(address_port)
        self.queue = SockQueue(self.sock)

    def send(self, proto_msg: betterproto.Message):
        msg = bytes(proto_msg)
        msg_len = self._encodeVarint(msg)
        self.sock.send(msg_len)
        self.sock.send(msg)

    def recv(self, proto_constructor: Callable[[], type(betterproto.Message)]) -> betterproto.Message:
        lenBytes = b""
        pos = 0

        while True:
            lenBytes += self.queue.get()
            if (lenBytes[pos] & 0x80) != 0x80:
                break
            pos += 1
        recv_len, new_pos = _DecodeVarint32(lenBytes, 0)
        buf = b''
        for i in range(recv_len):
            buf += self.queue.get()
        proto_msg = proto_constructor().parse(buf)
        return proto_msg
