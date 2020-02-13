from arena_lib.AiTankArenaServer import Weapon
from arena_lib.game.MyEntity import MyEntity
from arena_lib.game.State import State


class MyWeapon(MyEntity):

    def __init__(self, id: int, state: State, weapon: Weapon):
        super().__init__(id, state)
        self.weapon = weapon
