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

DESCRIPTOR = _descriptor.FileDescriptor(
  name='operation.proto',
  package='AiTankArenaServer',
  syntax='proto3',
  serialized_options=b'\n(cn.teamthevoid.AiTankArenaServer.messageP\001',
  serialized_pb=b'\n\x0foperation.proto\x12\x11\x41iTankArenaServer\"L\n\tOperation\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .AiTankArenaServer.OperationType\x12\x0f\n\x07message\x18\x02 \x01(\t*u\n\rOperationType\x12\x0e\n\nGET_STATUS\x10\x00\x12\x08\n\x04JOIN\x10\x01\x12\r\n\tAI_ACTION\x10\x02\x12\n\n\x06\x46RANCE\x10\x03\x12\x08\n\x04HALT\x10\x04\x12\x08\n\x04INIT\x10\x05\x12\n\n\x06REJOIN\x10\x06\x12\x0f\n\x0bSERVER_INFO\x10\x07\x42,\n(cn.teamthevoid.AiTankArenaServer.messageP\x01\x62\x06proto3'
)

_OPERATIONTYPE = _descriptor.EnumDescriptor(
  name='OperationType',
  full_name='AiTankArenaServer.OperationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET_STATUS', index=0, number=0,
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
      name='INIT', index=5, number=5,
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=116,
  serialized_end=233,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONTYPE)

OperationType = enum_type_wrapper.EnumTypeWrapper(_OPERATIONTYPE)
GET_STATUS = 0
JOIN = 1
AI_ACTION = 2
FRANCE = 3
HALT = 4
INIT = 5
REJOIN = 6
SERVER_INFO = 7

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
  serialized_start=38,
  serialized_end=114,
)

_OPERATION.fields_by_name['type'].enum_type = _OPERATIONTYPE
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.enum_types_by_name['OperationType'] = _OPERATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR': _OPERATION,
  '__module__': 'operation_pb2'
  # @@protoc_insertion_point(class_scope:AiTankArenaServer.Operation)
})
_sym_db.RegisterMessage(Operation)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
