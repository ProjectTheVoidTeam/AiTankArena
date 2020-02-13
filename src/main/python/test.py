from arena_lib.AiTankArenaServer import *
from arena_lib.ProtobufConnection import ProtobufConnection

opr = Operation()
opr.type = OperationType.DEBUG

conn = ProtobufConnection(('127.0.0.1', 8080))
conn.send(opr)
print(conn.recv(Response))
