# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

import game_pb2 as game__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='response.proto',
  package='AiTankArenaServer',
  syntax='proto3',
  serialized_options=b'\n1cn.teamthevoid.AiTankArenaServer.message.responseP\001',
  serialized_pb=b'\n\x0eresponse.proto\x12\x11\x41iTankArenaServer\x1a\ngame.proto\"\x94\x01\n\tGameState\x12+\n\x05stage\x18\x01 \x01(\x0e\x32\x1c.AiTankArenaServer.GameStage\x12&\n\x05tanks\x18\x02 \x03(\x0b\x32\x17.AiTankArenaServer.Tank\x12\x32\n\x0bprojections\x18\x03 \x03(\x0b\x32\x1d.AiTankArenaServer.Projection\"Z\n\nServerInfo\x12\x0f\n\x07\x62uildId\x18\x01 \x01(\x05\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x12\n\nserverName\x18\x03 \x01(\t\x12\x16\n\x0ewelcomeMessage\x18\x04 \x01(\t\"\xc5\x01\n\x08Response\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.AiTankArenaServer.Status\x12/\n\tgameState\x18\x02 \x01(\x0b\x32\x1c.AiTankArenaServer.GameState\x12*\n\x07players\x18\x03 \x03(\x0b\x32\x19.AiTankArenaServer.Player\x12\x31\n\nserverInfo\x18\x04 \x01(\x0b\x32\x1d.AiTankArenaServer.ServerInfo*1\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0cSERVER_ERROR\x10\x01\x12\r\n\tNOT_FOUND\x10\x02*=\n\tGameStage\x12\x0b\n\x07WAITING\x10\x00\x12\r\n\tALL_READY\x10\x01\x12\x0b\n\x07IN_GAME\x10\x02\x12\x07\n\x03\x45ND\x10\x03\x42\x35\n1cn.teamthevoid.AiTankArenaServer.message.responseP\x01\x62\x06proto3'
  ,
  dependencies=[game__pb2.DESCRIPTOR, ])

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='AiTankArenaServer.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=492,
  serialized_end=541,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_GAMESTAGE = _descriptor.EnumDescriptor(
  name='GameStage',
  full_name='AiTankArenaServer.GameStage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAITING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALL_READY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_GAME', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=543,
  serialized_end=604,
)
_sym_db.RegisterEnumDescriptor(_GAMESTAGE)

GameStage = enum_type_wrapper.EnumTypeWrapper(_GAMESTAGE)
OK = 0
SERVER_ERROR = 1
NOT_FOUND = 2
WAITING = 0
ALL_READY = 1
IN_GAME = 2
END = 3

_GAMESTATE = _descriptor.Descriptor(
  name='GameState',
  full_name='AiTankArenaServer.GameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage', full_name='AiTankArenaServer.GameState.stage', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tanks', full_name='AiTankArenaServer.GameState.tanks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projections', full_name='AiTankArenaServer.GameState.projections', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=50,
  serialized_end=198,
)

_SERVERINFO = _descriptor.Descriptor(
  name='ServerInfo',
  full_name='AiTankArenaServer.ServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buildId', full_name='AiTankArenaServer.ServerInfo.buildId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='AiTankArenaServer.ServerInfo.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serverName', full_name='AiTankArenaServer.ServerInfo.serverName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='welcomeMessage', full_name='AiTankArenaServer.ServerInfo.welcomeMessage', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=200,
  serialized_end=290,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='AiTankArenaServer.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='AiTankArenaServer.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameState', full_name='AiTankArenaServer.Response.gameState', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='players', full_name='AiTankArenaServer.Response.players', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serverInfo', full_name='AiTankArenaServer.Response.serverInfo', index=3,
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
  serialized_start=293,
  serialized_end=490,
)

_GAMESTATE.fields_by_name['stage'].enum_type = _GAMESTAGE
_GAMESTATE.fields_by_name['tanks'].message_type = game__pb2._TANK
_GAMESTATE.fields_by_name['projections'].message_type = game__pb2._PROJECTION
_RESPONSE.fields_by_name['status'].enum_type = _STATUS
_RESPONSE.fields_by_name['gameState'].message_type = _GAMESTATE
_RESPONSE.fields_by_name['players'].message_type = game__pb2._PLAYER
_RESPONSE.fields_by_name['serverInfo'].message_type = _SERVERINFO
DESCRIPTOR.message_types_by_name['GameState'] = _GAMESTATE
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
DESCRIPTOR.enum_types_by_name['GameStage'] = _GAMESTAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameState = _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {
  'DESCRIPTOR': _GAMESTATE,
  '__module__': 'response_pb2'
  # @@protoc_insertion_point(class_scope:AiTankArenaServer.GameState)
})
_sym_db.RegisterMessage(GameState)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), {
  'DESCRIPTOR': _SERVERINFO,
  '__module__': 'response_pb2'
  # @@protoc_insertion_point(class_scope:AiTankArenaServer.ServerInfo)
})
_sym_db.RegisterMessage(ServerInfo)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR': _RESPONSE,
  '__module__': 'response_pb2'
  # @@protoc_insertion_point(class_scope:AiTankArenaServer.Response)
})
_sym_db.RegisterMessage(Response)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)