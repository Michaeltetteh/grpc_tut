# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sayhello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sayhello.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0esayhello.proto\"\x1d\n\nRequestMsg\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"(\n\x0bResponseMsg\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t21\n\x08SayHello\x12%\n\x08SayHello\x12\x0b.RequestMsg\x1a\x0c.ResponseMsgb\x06proto3'
)




_REQUESTMSG = _descriptor.Descriptor(
  name='RequestMsg',
  full_name='RequestMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='RequestMsg.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=18,
  serialized_end=47,
)


_RESPONSEMSG = _descriptor.Descriptor(
  name='ResponseMsg',
  full_name='ResponseMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ResponseMsg.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='ResponseMsg.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=49,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['RequestMsg'] = _REQUESTMSG
DESCRIPTOR.message_types_by_name['ResponseMsg'] = _RESPONSEMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestMsg = _reflection.GeneratedProtocolMessageType('RequestMsg', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTMSG,
  '__module__' : 'sayhello_pb2'
  # @@protoc_insertion_point(class_scope:RequestMsg)
  })
_sym_db.RegisterMessage(RequestMsg)

ResponseMsg = _reflection.GeneratedProtocolMessageType('ResponseMsg', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEMSG,
  '__module__' : 'sayhello_pb2'
  # @@protoc_insertion_point(class_scope:ResponseMsg)
  })
_sym_db.RegisterMessage(ResponseMsg)



_SAYHELLO = _descriptor.ServiceDescriptor(
  name='SayHello',
  full_name='SayHello',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=91,
  serialized_end=140,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='SayHello.SayHello',
    index=0,
    containing_service=None,
    input_type=_REQUESTMSG,
    output_type=_RESPONSEMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SAYHELLO)

DESCRIPTOR.services_by_name['SayHello'] = _SAYHELLO

# @@protoc_insertion_point(module_scope)