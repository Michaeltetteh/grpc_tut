# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: django_grpc/main.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='django_grpc/main.proto',
  package='django_grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x64jango_grpc/main.proto\x12\x0b\x64jango_grpc\"\x17\n\x04Ping\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x17\n\x04Pong\x12\x0f\n\x07message\x18\x01 \x01(\t\"@\n\x0cSystemEntity\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\"K\n\tSystemRun\x12\x11\n\tsystem_id\x18\x01 \x01(\t\x12+\n\x08\x65ntities\x18\x02 \x03(\x0b\x32\x19.django_grpc.SystemEntity\"#\n\x11SystemRunResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\t\"Z\n\nActivation\x12\x11\n\tsystem_id\x18\x01 \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\t\x12)\n\x06\x65ntity\x18\x03 \x01(\x0b\x32\x19.django_grpc.SystemEntity\"%\n\x12\x41\x63tivationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xd0\x01\n\x04Main\x12.\n\x04ping\x12\x11.django_grpc.Ping\x1a\x11.django_grpc.Pong\"\x00\x12J\n\x0enew_system_run\x12\x16.django_grpc.SystemRun\x1a\x1e.django_grpc.SystemRunResponse\"\x00\x12L\n\x0enew_activation\x12\x17.django_grpc.Activation\x1a\x1f.django_grpc.ActivationResponse\"\x00\x62\x06proto3'
)




_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='django_grpc.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='django_grpc.Ping.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=39,
  serialized_end=62,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='django_grpc.Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='django_grpc.Pong.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=64,
  serialized_end=87,
)


_SYSTEMENTITY = _descriptor.Descriptor(
  name='SystemEntity',
  full_name='django_grpc.SystemEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='django_grpc.SystemEntity.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='django_grpc.SystemEntity.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identity', full_name='django_grpc.SystemEntity.identity', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=89,
  serialized_end=153,
)


_SYSTEMRUN = _descriptor.Descriptor(
  name='SystemRun',
  full_name='django_grpc.SystemRun',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='system_id', full_name='django_grpc.SystemRun.system_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entities', full_name='django_grpc.SystemRun.entities', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=155,
  serialized_end=230,
)


_SYSTEMRUNRESPONSE = _descriptor.Descriptor(
  name='SystemRunResponse',
  full_name='django_grpc.SystemRunResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='run_id', full_name='django_grpc.SystemRunResponse.run_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=232,
  serialized_end=267,
)


_ACTIVATION = _descriptor.Descriptor(
  name='Activation',
  full_name='django_grpc.Activation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='system_id', full_name='django_grpc.Activation.system_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='run_id', full_name='django_grpc.Activation.run_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity', full_name='django_grpc.Activation.entity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=269,
  serialized_end=359,
)


_ACTIVATIONRESPONSE = _descriptor.Descriptor(
  name='ActivationResponse',
  full_name='django_grpc.ActivationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='django_grpc.ActivationResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=361,
  serialized_end=398,
)

_SYSTEMRUN.fields_by_name['entities'].message_type = _SYSTEMENTITY
_ACTIVATION.fields_by_name['entity'].message_type = _SYSTEMENTITY
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
DESCRIPTOR.message_types_by_name['SystemEntity'] = _SYSTEMENTITY
DESCRIPTOR.message_types_by_name['SystemRun'] = _SYSTEMRUN
DESCRIPTOR.message_types_by_name['SystemRunResponse'] = _SYSTEMRUNRESPONSE
DESCRIPTOR.message_types_by_name['Activation'] = _ACTIVATION
DESCRIPTOR.message_types_by_name['ActivationResponse'] = _ACTIVATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), {
  'DESCRIPTOR' : _PING,
  '__module__' : 'django_grpc.main_pb2'
  # @@protoc_insertion_point(class_scope:django_grpc.Ping)
  })
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), {
  'DESCRIPTOR' : _PONG,
  '__module__' : 'django_grpc.main_pb2'
  # @@protoc_insertion_point(class_scope:django_grpc.Pong)
  })
_sym_db.RegisterMessage(Pong)

SystemEntity = _reflection.GeneratedProtocolMessageType('SystemEntity', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMENTITY,
  '__module__' : 'django_grpc.main_pb2'
  # @@protoc_insertion_point(class_scope:django_grpc.SystemEntity)
  })
_sym_db.RegisterMessage(SystemEntity)

SystemRun = _reflection.GeneratedProtocolMessageType('SystemRun', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMRUN,
  '__module__' : 'django_grpc.main_pb2'
  # @@protoc_insertion_point(class_scope:django_grpc.SystemRun)
  })
_sym_db.RegisterMessage(SystemRun)

SystemRunResponse = _reflection.GeneratedProtocolMessageType('SystemRunResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMRUNRESPONSE,
  '__module__' : 'django_grpc.main_pb2'
  # @@protoc_insertion_point(class_scope:django_grpc.SystemRunResponse)
  })
_sym_db.RegisterMessage(SystemRunResponse)

Activation = _reflection.GeneratedProtocolMessageType('Activation', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATION,
  '__module__' : 'django_grpc.main_pb2'
  # @@protoc_insertion_point(class_scope:django_grpc.Activation)
  })
_sym_db.RegisterMessage(Activation)

ActivationResponse = _reflection.GeneratedProtocolMessageType('ActivationResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONRESPONSE,
  '__module__' : 'django_grpc.main_pb2'
  # @@protoc_insertion_point(class_scope:django_grpc.ActivationResponse)
  })
_sym_db.RegisterMessage(ActivationResponse)



_MAIN = _descriptor.ServiceDescriptor(
  name='Main',
  full_name='django_grpc.Main',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=401,
  serialized_end=609,
  methods=[
  _descriptor.MethodDescriptor(
    name='ping',
    full_name='django_grpc.Main.ping',
    index=0,
    containing_service=None,
    input_type=_PING,
    output_type=_PONG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_system_run',
    full_name='django_grpc.Main.new_system_run',
    index=1,
    containing_service=None,
    input_type=_SYSTEMRUN,
    output_type=_SYSTEMRUNRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_activation',
    full_name='django_grpc.Main.new_activation',
    index=2,
    containing_service=None,
    input_type=_ACTIVATION,
    output_type=_ACTIVATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAIN)

DESCRIPTOR.services_by_name['Main'] = _MAIN

# @@protoc_insertion_point(module_scope)
