from arena_lib.AiTankArenaServer import *
from arena_lib.ArenaServerConnection import ArenaServerConnection

from arena_lib.game.MyTank import MyTank
from arena_lib.game.State import State


class AI():
    def __init__(self):
        super().__init__()
        self.conn: ArenaServerConnection = None
        self.player_id = -1
        self.my_tank: MyTank = None

    def connect(self, host: str, port: int):
        try:
            self.conn = ArenaServerConnection((host, port))
        except:
            print("Connect to server failed")
            exit(1)
        print("Connect to server success")

    def is_opr_success(self):
        self.conn.recv().status == Status.OK

    def join(self, room_id: int, my_name: str) -> bool:
        opr = Operation()
        opr.type = OperationType.JOIN
        opr.join_room_info.room_id = room_id
        opr.join_room_info.my_player_name = my_name
        opr.join_room_info.type = PlayerType.WARRIOR
        self.conn.send(opr)
        result = self.conn.recv()
        if result.status == Status.OK:
            print("Join room:%d success" % room_id)
            self.player_id = result.your_player_id
            self.my_tank = MyTank(self.player_id, State(result.game_state))
            return True
        else:
            print("Join room:%d failed" % room_id)
            return False

    def ready(self):
        opr = Operation(type=OperationType.READY)
        self.conn.send(opr)
        self.start_loop()

    def start_game(self, room_id: int, my_name="Unamed AI", host="127.0.0.1", port=8080):
        self.connect(host, port)
        if self.join(room_id, my_name):
            self.ready()
            self.start_loop()

        else:
            exit(1)

    def start_loop(self):
        while True:
            self._next_tick()

    def action(self, state: State, my_tank: Tank):
        raise Exception("You must implement action method")

    def _next_tick(self):
        res = self.conn.recv()
        stage = res.game_state.stage
        if stage == GameStage.IN_GAME or GameStage.ALL_READY:
            state = State(res.game_state)
            self.my_tank.update(state)
            self.action(state, self.my_tank)
            opr = Operation()
            opr.actions = state.actions.values()
            opr.type = OperationType.ACTION
            self.conn.send(opr)
        if stage == GameStage.WAITING or GameStage.ALL_READY:
            print("Ready state change:")
            print(res)
        if stage == GameStage.ALL_READY:
            print("All AIs are ready,game will start")
