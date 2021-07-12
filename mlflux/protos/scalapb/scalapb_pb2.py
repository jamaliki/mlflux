# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scalapb/scalapb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='scalapb/scalapb.proto',
  package='scalapb',
  syntax='proto2',
  serialized_options=_b('\n\034org.mlflux.scalapb_interface'),
  serialized_pb=_b('\n\x15scalapb/scalapb.proto\x12\x07scalapb\x1a google/protobuf/descriptor.proto\"L\n\x0eScalaPbOptions\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x14\n\x0c\x66lat_package\x18\x02 \x01(\x08\x12\x0e\n\x06import\x18\x03 \x03(\t\"!\n\x0eMessageOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t\"\x1c\n\x0c\x46ieldOptions\x12\x0c\n\x04type\x18\x01 \x01(\t:G\n\x07options\x12\x1c.google.protobuf.FileOptions\x18\xfc\x07 \x01(\x0b\x32\x17.scalapb.ScalaPbOptions:J\n\x07message\x12\x1f.google.protobuf.MessageOptions\x18\xfc\x07 \x01(\x0b\x32\x17.scalapb.MessageOptions:D\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\xfc\x07 \x01(\x0b\x32\x15.scalapb.FieldOptionsB\x1e\n\x1corg.mlflux.scalapb_interface')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


OPTIONS_FIELD_NUMBER = 1020
options = _descriptor.FieldDescriptor(
  name='options', full_name='scalapb.options', index=0,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
MESSAGE_FIELD_NUMBER = 1020
message = _descriptor.FieldDescriptor(
  name='message', full_name='scalapb.message', index=1,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
FIELD_FIELD_NUMBER = 1020
field = _descriptor.FieldDescriptor(
  name='field', full_name='scalapb.field', index=2,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_SCALAPBOPTIONS = _descriptor.Descriptor(
  name='ScalaPbOptions',
  full_name='scalapb.ScalaPbOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_name', full_name='scalapb.ScalaPbOptions.package_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flat_package', full_name='scalapb.ScalaPbOptions.flat_package', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='import', full_name='scalapb.ScalaPbOptions.import', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=144,
)


_MESSAGEOPTIONS = _descriptor.Descriptor(
  name='MessageOptions',
  full_name='scalapb.MessageOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extends', full_name='scalapb.MessageOptions.extends', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=179,
)


_FIELDOPTIONS = _descriptor.Descriptor(
  name='FieldOptions',
  full_name='scalapb.FieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='scalapb.FieldOptions.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['ScalaPbOptions'] = _SCALAPBOPTIONS
DESCRIPTOR.message_types_by_name['MessageOptions'] = _MESSAGEOPTIONS
DESCRIPTOR.message_types_by_name['FieldOptions'] = _FIELDOPTIONS
DESCRIPTOR.extensions_by_name['options'] = options
DESCRIPTOR.extensions_by_name['message'] = message
DESCRIPTOR.extensions_by_name['field'] = field
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScalaPbOptions = _reflection.GeneratedProtocolMessageType('ScalaPbOptions', (_message.Message,), dict(
  DESCRIPTOR = _SCALAPBOPTIONS,
  __module__ = 'scalapb.scalapb_pb2'
  # @@protoc_insertion_point(class_scope:scalapb.ScalaPbOptions)
  ))
_sym_db.RegisterMessage(ScalaPbOptions)

MessageOptions = _reflection.GeneratedProtocolMessageType('MessageOptions', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEOPTIONS,
  __module__ = 'scalapb.scalapb_pb2'
  # @@protoc_insertion_point(class_scope:scalapb.MessageOptions)
  ))
_sym_db.RegisterMessage(MessageOptions)

FieldOptions = _reflection.GeneratedProtocolMessageType('FieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _FIELDOPTIONS,
  __module__ = 'scalapb.scalapb_pb2'
  # @@protoc_insertion_point(class_scope:scalapb.FieldOptions)
  ))
_sym_db.RegisterMessage(FieldOptions)

options.message_type = _SCALAPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(options)
message.message_type = _MESSAGEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message)
field.message_type = _FIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)