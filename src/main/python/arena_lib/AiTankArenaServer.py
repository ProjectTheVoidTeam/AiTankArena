# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: share.proto, game.proto, operation.proto, response.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class PlayerType(betterproto.Enum):
    """玩家类型"""

    WARRIOR = 0
    OBSERVER = 1


class WeaponType(betterproto.Enum):
    CANNON = 0


class WeaponState(betterproto.Enum):
    IDLE = 0
    ACTIVE = 1
    COOL_DOWN = 2


class ProjectionType(betterproto.Enum):
    BALL = 0


class ActionType(betterproto.Enum):
    ENABLE = 0
    DISABLE = 1


class OperationType(betterproto.Enum):
    GET_STATE = 0
    JOIN = 1
    ACTION = 2
    FRANCE = 3
    HALT = 4
    READY = 5
    REJOIN = 6
    SERVER_INFO = 7
    DEBUG = 8


class Status(betterproto.Enum):
    SERVER_ERROR = 0
    OK = 1
    NOT_FOUND = 2


class GameStage(betterproto.Enum):
    WAITING = 0
    ALL_READY = 1
    IN_GAME = 2
    END = 3


@dataclass
class Vector2D(betterproto.Message):
    """2维向量"""

    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)


@dataclass
class Vector3D(betterproto.Message):
    """3维向量"""

    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)
    z: float = betterproto.float_field(3)


@dataclass
class Rect(betterproto.Message):
    pos_top_left: float = betterproto.float_field(1)
    pos_bottom_right: float = betterproto.float_field(2)


@dataclass
class Player(betterproto.Message):
    """游戏玩家"""

    id: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    is_ready: bool = betterproto.bool_field(3)
    spawn_point_id: int = betterproto.uint32_field(4)
    type: "PlayerType" = betterproto.enum_field(6)
    tank_id: int = betterproto.uint32_field(7)
    player_results: "PlayerResults" = betterproto.message_field(5)


@dataclass
class PlayerResults(betterproto.Message):
    """结算状态信息"""

    is_winner: bool = betterproto.bool_field(1)
    kill: int = betterproto.int32_field(2)
    death: int = betterproto.int32_field(3)
    assistant: int = betterproto.int32_field(4)
    damage: int = betterproto.int32_field(5)


@dataclass
class Tank(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    pos: "Vector2D" = betterproto.message_field(2)
    direction: "Vector2D" = betterproto.message_field(3)
    hitbox: "Rect" = betterproto.message_field(4)
    weapons: List["Weapon"] = betterproto.message_field(5)


@dataclass
class Weapon(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    type: "WeaponType" = betterproto.enum_field(2)
    state: "WeaponState" = betterproto.enum_field(3)


@dataclass
class Projection(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    pos: "Vector2D" = betterproto.message_field(2)
    direction: "Vector2D" = betterproto.message_field(3)
    type: "ProjectionType" = betterproto.enum_field(4)


@dataclass
class Action(betterproto.Message):
    source_id: int = betterproto.int32_field(1)
    type: "ActionType" = betterproto.enum_field(2)
    direction: "Vector2D" = betterproto.message_field(3)
    power: float = betterproto.float_field(4)
    target_pos: "Vector2D" = betterproto.message_field(5)
    target_id: "Vector2D" = betterproto.message_field(6)


@dataclass
class JoinRoomInfo(betterproto.Message):
    room_id: int = betterproto.int32_field(1)
    type: "PlayerType" = betterproto.enum_field(2)
    my_player_name: str = betterproto.string_field(3)
    spawn_point_id: int = betterproto.int32_field(4)
    weapons: List["Weapon"] = betterproto.message_field(5)


@dataclass
class Operation(betterproto.Message):
    type: "OperationType" = betterproto.enum_field(1)
    message: str = betterproto.string_field(2)
    join_room_info: "JoinRoomInfo" = betterproto.message_field(3)
    actions: List["Action"] = betterproto.message_field(4)


@dataclass
class GameState(betterproto.Message):
    """游戏战局状态"""

    stage: "GameStage" = betterproto.enum_field(1)
    tanks: List["Tank"] = betterproto.message_field(2)
    projections: List["Projection"] = betterproto.message_field(3)


@dataclass
class ServerInfo(betterproto.Message):
    build_id: int = betterproto.int32_field(1)
    version: str = betterproto.string_field(2)
    server_name: str = betterproto.string_field(3)
    welcome_message: str = betterproto.string_field(4)


@dataclass
class Response(betterproto.Message):
    status: "Status" = betterproto.enum_field(1)
    game_state: "GameState" = betterproto.message_field(2)
    players: List["Player"] = betterproto.message_field(3)
    server_info: "ServerInfo" = betterproto.message_field(4)
    your_player_id: int = betterproto.int32_field(5)
