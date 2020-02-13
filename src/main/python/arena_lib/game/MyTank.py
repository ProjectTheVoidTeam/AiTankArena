from arena_lib.AiTankArenaServer import Vector2D, Action
from arena_lib.game.MyEntity import MyEntity
from arena_lib.game.MyWeapon import MyWeapon
from arena_lib.game.State import State


class MyTank(MyEntity):

    def __init__(self, id: int, state: State):
        super().__init__(id, state)
        self.weapons: {str: MyWeapon} = {}  # WeaponName -> MyWeapon
        self.state = state

    def update(self, new_state: State):
        self.state = new_state
        for name, weapon in enumerate(self.weapons):
            my_tank = new_state.get_tank(self.id)
            assert my_tank is not None
            find_weapons = list(filter(lambda x: x.id == weapon.id, my_tank.weapons))
            assert len(find_weapons) == 1
            self.weapons[name] = MyWeapon(weapon.id, new_state, find_weapons[0])

    def move(self, direction: Vector2D):
        action = Action()
        action.source_id = self.id
        action.direction = direction
        self.actions[id] = action
