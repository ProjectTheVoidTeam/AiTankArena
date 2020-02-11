# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operation.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

import game_pb2 as game__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='operation.proto',
    package='AiTankArenaServer',
    syntax='proto3',
    serialized_options=b'\n2cn.teamthevoid.AiTankArenaServer.message.operationP\001',
    serialized_pb=b'\n\x0foperation.proto\x12\x11\x41iTankArenaServer\x1a\ngame.proto\"\xa3\x01\n\x0cJoinRoomInfo\x12\x0e\n\x06roomID\x18\x01 \x01(\x05\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.AiTankArenaServer.PlayerType\x12\x14\n\x0cmyPlayerName\x18\x03 \x01(\t\x12\x14\n\x0cspawnPointID\x18\x04 \x01(\x05\x12*\n\x07weapons\x18\x05 \x03(\x0b\x32\x19.AiTankArenaServer.Weapon\"\x83\x01\n\tOperation\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .AiTankArenaServer.OperationType\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x0cjoinRoomInfo\x18\x03 \x01(\x0b\x32\x1f.AiTankArenaServer.JoinRoomInfo*\x80\x01\n\rOperationType\x12\r\n\tGET_STATE\x10\x00\x12\x08\n\x04JOIN\x10\x01\x12\r\n\tAI_ACTION\x10\x02\x12\n\n\x06\x46RANCE\x10\x03\x12\x08\n\x04HALT\x10\x04\x12\t\n\x05READY\x10\x05\x12\n\n\x06REJOIN\x10\x06\x12\x0f\n\x0bSERVER_INFO\x10\x07\x12\t\n\x05\x44\x45\x42UG\x10\x08\x42\x36\n2cn.teamthevoid.AiTankArenaServer.message.operationP\x01\x62\x06proto3'
    ,
    dependencies=[game__pb2.DESCRIPTOR, ])

_OPERATIONTYPE = _descriptor.EnumDescriptor(
  name='OperationType',
  full_name='AiTankArenaServer.OperationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
        name='GET_STATE', index=0, number=0,
        serialized_options=None,
        type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AI_ACTION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRANCE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
        name='READY', index=5, number=5,
        serialized_options=None,
        type=None),
      _descriptor.EnumValueDescriptor(
          name='REJOIN', index=6, number=6,
          serialized_options=None,
          type=None),
      _descriptor.EnumValueDescriptor(
          name='SERVER_INFO', index=7, number=7,
          serialized_options=None,
          type=None),
      _descriptor.EnumValueDescriptor(
          name='DEBUG', index=8, number=8,
          serialized_options=None,
          type=None),
  ],
    containing_type=None,
    serialized_options=None,
    serialized_start=351,
    serialized_end=479,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONTYPE)

OperationType = enum_type_wrapper.EnumTypeWrapper(_OPERATIONTYPE)
GET_STATE = 0
JOIN = 1
AI_ACTION = 2
FRANCE = 3
HALT = 4
READY = 5
REJOIN = 6
SERVER_INFO = 7
DEBUG = 8

_JOINROOMINFO = _descriptor.Descriptor(
    name='JoinRoomInfo',
    full_name='AiTankArenaServer.JoinRoomInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='roomID', full_name='AiTankArenaServer.JoinRoomInfo.roomID', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='type', full_name='AiTankArenaServer.JoinRoomInfo.type', index=1,
            number=2, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='myPlayerName', full_name='AiTankArenaServer.JoinRoomInfo.myPlayerName', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='spawnPointID', full_name='AiTankArenaServer.JoinRoomInfo.spawnPointID', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='weapons', full_name='AiTankArenaServer.JoinRoomInfo.weapons', index=4,
            number=5, type=11, cpp_type=10, label=3,
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
    serialized_start=51,
    serialized_end=214,
)

_OPERATION = _descriptor.Descriptor(
    name='Operation',
    full_name='AiTankArenaServer.Operation',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
      name='type', full_name='AiTankArenaServer.Operation.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='message', full_name='AiTankArenaServer.Operation.message', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='joinRoomInfo', full_name='AiTankArenaServer.Operation.joinRoomInfo', index=2,
            number=3, type=11, cpp_type=10, label=1,
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
    serialized_start=217,
    serialized_end=348,
)

_JOINROOMINFO.fields_by_name['type'].enum_type = game__pb2._PLAYERTYPE
_JOINROOMINFO.fields_by_name['weapons'].message_type = game__pb2._WEAPON
_OPERATION.fields_by_name['type'].enum_type = _OPERATIONTYPE
_OPERATION.fields_by_name['joinRoomInfo'].message_type = _JOINROOMINFO
DESCRIPTOR.message_types_by_name['JoinRoomInfo'] = _JOINROOMINFO
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.enum_types_by_name['OperationType'] = _OPERATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JoinRoomInfo = _reflection.GeneratedProtocolMessageType('JoinRoomInfo', (_message.Message,), {
    'DESCRIPTOR': _JOINROOMINFO,
    '__module__': 'operation_pb2'
    # @@protoc_insertion_point(class_scope:AiTankArenaServer.JoinRoomInfo)
})
_sym_db.RegisterMessage(JoinRoomInfo)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
    'DESCRIPTOR': _OPERATION,
    '__module__': 'operation_pb2'
    # @@protoc_insertion_point(class_scope:AiTankArenaServer.Operation)
})
_sym_db.RegisterMessage(Operation)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
