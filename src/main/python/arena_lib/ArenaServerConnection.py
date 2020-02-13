from arena_lib.AiTankArenaServer import Response, Operation
from arena_lib.ProtobufConnection import *


class ArenaServerConnection(ProtobufConnection):

    def send(self, proto_msg: Operation):
        super().send(proto_msg)

    def recv(self) -> Response:
        return super().recv(Response)
