from arena_lib.game.State import State


class MyEntity:

    def __init__(self, id: int, state: State):
        self.actions = state.actions
        self.id = id
