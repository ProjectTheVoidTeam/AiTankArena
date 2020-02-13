# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

import share_pb2 as share__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='AiTankArenaServer',
  syntax='proto3',
  serialized_options=b'\n2cn.teamthevoid.AiTankArenaServer.message.operationP\001',
  serialized_pb=b'\n\ngame.proto\x12\x11\x41iTankArenaServer\x1a\x0bshare.proto\"\xbf\x01\n\x06Player\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07isReady\x18\x03 \x01(\x08\x12\x14\n\x0cspawnPointId\x18\x04 \x01(\r\x12+\n\x04type\x18\x06 \x01(\x0e\x32\x1d.AiTankArenaServer.PlayerType\x12\x0e\n\x06tankId\x18\x07 \x01(\r\x12\x37\n\rplayerResults\x18\x05 \x01(\x0b\x32 .AiTankArenaServer.PlayerResults\"a\n\rPlayerResults\x12\x10\n\x08isWinner\x18\x01 \x01(\x08\x12\x0c\n\x04kill\x18\x02 \x01(\x05\x12\r\n\x05\x64\x65\x61th\x18\x03 \x01(\x05\x12\x11\n\tassistant\x18\x04 \x01(\x05\x12\x0e\n\x06\x64\x61mage\x18\x05 \x01(\x05\"\x95\x01\n\x04Tank\x12\n\n\x02id\x18\x01 \x01(\r\x12(\n\x03pos\x18\x02 \x01(\x0b\x32\x1b.AiTankArenaServer.Vector2D\x12.\n\tdirection\x18\x03 \x01(\x0b\x32\x1b.AiTankArenaServer.Vector2D\x12\'\n\x06hitbox\x18\x04 \x01(\x0b\x32\x17.AiTankArenaServer.Rect\"p\n\x06Weapon\x12\n\n\x02id\x18\x01 \x01(\r\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.AiTankArenaServer.WeaponType\x12-\n\x05state\x18\x03 \x01(\x0e\x32\x1e.AiTankArenaServer.WeaponState\"\xa3\x01\n\nProjection\x12\n\n\x02id\x18\x01 \x01(\r\x12(\n\x03pos\x18\x02 \x01(\x0b\x32\x1b.AiTankArenaServer.Vector2D\x12.\n\tdirection\x18\x03 \x01(\x0b\x32\x1b.AiTankArenaServer.Vector2D\x12/\n\x04type\x18\x04 \x01(\x0e\x32!.AiTankArenaServer.ProjectionType*\'\n\nPlayerType\x12\x0b\n\x07WARRIOR\x10\x00\x12\x0c\n\x08OBSERVER\x10\x01*\x18\n\nWeaponType\x12\n\n\x06\x43\x41NNON\x10\x00*2\n\x0bWeaponState\x12\x08\n\x04IDLE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\r\n\tCOOL_DOWN\x10\x02*\x1a\n\x0eProjectionType\x12\x08\n\x04\x42\x41LL\x10\x00\x42\x36\n2cn.teamthevoid.AiTankArenaServer.message.operationP\x01\x62\x06proto3'
  ,
  dependencies=[share__pb2.DESCRIPTOR, ])

_PLAYERTYPE = _descriptor.EnumDescriptor(
  name='PlayerType',
  full_name='AiTankArenaServer.PlayerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WARRIOR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OBSERVER', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=771,
  serialized_end=810,
)
_sym_db.RegisterEnumDescriptor(_PLAYERTYPE)

PlayerType = enum_type_wrapper.EnumTypeWrapper(_PLAYERTYPE)
_WEAPONTYPE = _descriptor.EnumDescriptor(
  name='WeaponType',
  full_name='AiTankArenaServer.WeaponType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CANNON', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=812,
  serialized_end=836,
)
_sym_db.RegisterEnumDescriptor(_WEAPONTYPE)

WeaponType = enum_type_wrapper.EnumTypeWrapper(_WEAPONTYPE)
_WEAPONSTATE = _descriptor.EnumDescriptor(
  name='WeaponState',
  full_name='AiTankArenaServer.WeaponState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COOL_DOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=838,
  serialized_end=888,
)
_sym_db.RegisterEnumDescriptor(_WEAPONSTATE)

WeaponState = enum_type_wrapper.EnumTypeWrapper(_WEAPONSTATE)
_PROJECTIONTYPE = _descriptor.EnumDescriptor(
  name='ProjectionType',
  full_name='AiTankArenaServer.ProjectionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BALL', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=890,
  serialized_end=916,
)
_sym_db.RegisterEnumDescriptor(_PROJECTIONTYPE)

ProjectionType = enum_type_wrapper.EnumTypeWrapper(_PROJECTIONTYPE)
WARRIOR = 0
OBSERVER = 1
CANNON = 0
IDLE = 0
ACTIVE = 1
COOL_DOWN = 2
BALL = 0

_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='AiTankArenaServer.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AiTankArenaServer.Player.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='AiTankArenaServer.Player.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isReady', full_name='AiTankArenaServer.Player.isReady', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spawnPointId', full_name='AiTankArenaServer.Player.spawnPointId', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='AiTankArenaServer.Player.type', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tankId', full_name='AiTankArenaServer.Player.tankId', index=5,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playerResults', full_name='AiTankArenaServer.Player.playerResults', index=6,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=238,
)

_PLAYERRESULTS = _descriptor.Descriptor(
  name='PlayerResults',
  full_name='AiTankArenaServer.PlayerResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isWinner', full_name='AiTankArenaServer.PlayerResults.isWinner', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kill', full_name='AiTankArenaServer.PlayerResults.kill', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='death', full_name='AiTankArenaServer.PlayerResults.death', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assistant', full_name='AiTankArenaServer.PlayerResults.assistant', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='damage', full_name='AiTankArenaServer.PlayerResults.damage', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=337,
)

_TANK = _descriptor.Descriptor(
  name='Tank',
  full_name='AiTankArenaServer.Tank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AiTankArenaServer.Tank.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='AiTankArenaServer.Tank.pos', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='AiTankArenaServer.Tank.direction', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hitbox', full_name='AiTankArenaServer.Tank.hitbox', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=489,
)

_WEAPON = _descriptor.Descriptor(
  name='Weapon',
  full_name='AiTankArenaServer.Weapon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AiTankArenaServer.Weapon.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='AiTankArenaServer.Weapon.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='AiTankArenaServer.Weapon.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=491,
  serialized_end=603,
)

_PROJECTION = _descriptor.Descriptor(
  name='Projection',
  full_name='AiTankArenaServer.Projection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AiTankArenaServer.Projection.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='AiTankArenaServer.Projection.pos', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='AiTankArenaServer.Projection.direction', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='AiTankArenaServer.Projection.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=769,
)

_PLAYER.fields_by_name['type'].enum_type = _PLAYERTYPE
_PLAYER.fields_by_name['playerResults'].message_type = _PLAYERRESULTS
_TANK.fields_by_name['pos'].message_type = share__pb2._VECTOR2D
_TANK.fields_by_name['direction'].message_type = share__pb2._VECTOR2D
_TANK.fields_by_name['hitbox'].message_type = share__pb2._RECT
_WEAPON.fields_by_name['type'].enum_type = _WEAPONTYPE
_WEAPON.fields_by_name['state'].enum_type = _WEAPONSTATE
_PROJECTION.fields_by_name['pos'].message_type = share__pb2._VECTOR2D
_PROJECTION.fields_by_name['direction'].message_type = share__pb2._VECTOR2D
_PROJECTION.fields_by_name['type'].enum_type = _PROJECTIONTYPE
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['PlayerResults'] = _PLAYERRESULTS
DESCRIPTOR.message_types_by_name['Tank'] = _TANK
DESCRIPTOR.message_types_by_name['Weapon'] = _WEAPON
DESCRIPTOR.message_types_by_name['Projection'] = _PROJECTION
DESCRIPTOR.enum_types_by_name['PlayerType'] = _PLAYERTYPE
DESCRIPTOR.enum_types_by_name['WeaponType'] = _WEAPONTYPE
DESCRIPTOR.enum_types_by_name['WeaponState'] = _WEAPONSTATE
DESCRIPTOR.enum_types_by_name['ProjectionType'] = _PROJECTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR': _PLAYER,
  '__module__': 'game_pb2'
  # @@protoc_insertion_point(class_scope:AiTankArenaServer.Player)
})
_sym_db.RegisterMessage(Player)

PlayerResults = _reflection.GeneratedProtocolMessageType('PlayerResults', (_message.Message,), {
  'DESCRIPTOR': _PLAYERRESULTS,
  '__module__': 'game_pb2'
  # @@protoc_insertion_point(class_scope:AiTankArenaServer.PlayerResults)
})
_sym_db.RegisterMessage(PlayerResults)

Tank = _reflection.GeneratedProtocolMessageType('Tank', (_message.Message,), {
  'DESCRIPTOR': _TANK,
  '__module__': 'game_pb2'
  # @@protoc_insertion_point(class_scope:AiTankArenaServer.Tank)
})
_sym_db.RegisterMessage(Tank)

Weapon = _reflection.GeneratedProtocolMessageType('Weapon', (_message.Message,), {
  'DESCRIPTOR': _WEAPON,
  '__module__': 'game_pb2'
  # @@protoc_insertion_point(class_scope:AiTankArenaServer.Weapon)
})
_sym_db.RegisterMessage(Weapon)

Projection = _reflection.GeneratedProtocolMessageType('Projection', (_message.Message,), {
  'DESCRIPTOR': _PROJECTION,
  '__module__': 'game_pb2'
  # @@protoc_insertion_point(class_scope:AiTankArenaServer.Projection)
})
_sym_db.RegisterMessage(Projection)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)