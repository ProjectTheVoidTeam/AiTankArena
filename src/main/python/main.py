from arena_lib.AI import AI
from arena_lib.AiTankArenaServer import Tank
from arena_lib.game.State import State


class MyTestAI(AI):

    def action(self, state: State, my_tank: Tank):
        print(state)
        pass


ai = MyTestAI()
ai.start_game(0)
