from arena_lib.AiTankArenaServer import GameState, Action


class State:

    def __init__(self, gameState: GameState) -> None:
        self.tanks = gameState.tanks
        self.projections = gameState.projections
        self.actions: {int: Action} = {}  # sourceId->Action 将要被发送的Action的dict

    def get_tank(self, id):
        tanks = list(filter(lambda it: it.id == id, self.tanks))
        if len(tanks) == 0:
            return None
        else:
            return tanks[0]
