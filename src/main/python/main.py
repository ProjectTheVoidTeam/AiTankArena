import operation_pb2 as proto
from protobuf_connection import ProtobufConnection

opr = proto.Operation()
opr.type = proto.AI_ACTION
opr.message = "Hello World"

conn = ProtobufConnection(('127.0.0.1', 8080))
conn.send(opr)
print(conn.recv(proto.Operation))
