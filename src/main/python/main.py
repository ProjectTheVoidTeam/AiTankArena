import operation_pb2 as operation_pb
import response_pb2 as response_pb
from protobuf_connection import ProtobufConnection

opr = operation_pb.Operation()
opr.type = operation_pb.JOIN
opr.message = "Hello World"

conn = ProtobufConnection(('127.0.0.1', 8080))
conn.send(opr)
print(conn.recv(response_pb.Response))
conn.send(opr)
print(conn.recv(response_pb.Response))
