# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: consensus_create_topic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2
import duration_pb2 as duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='consensus_create_topic.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x63onsensus_create_topic.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0e\x64uration.proto\"\xc6\x01\n#ConsensusCreateTopicTransactionBody\x12\x0c\n\x04memo\x18\x01 \x01(\t\x12\x1c\n\x08\x61\x64minKey\x18\x02 \x01(\x0b\x32\n.proto.Key\x12\x1d\n\tsubmitKey\x18\x03 \x01(\x0b\x32\n.proto.Key\x12(\n\x0f\x61utoRenewPeriod\x18\x06 \x01(\x0b\x32\x0f.proto.Duration\x12*\n\x10\x61utoRenewAccount\x18\x07 \x01(\x0b\x32\x10.proto.AccountIDB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,duration__pb2.DESCRIPTOR,])




_CONSENSUSCREATETOPICTRANSACTIONBODY = _descriptor.Descriptor(
  name='ConsensusCreateTopicTransactionBody',
  full_name='proto.ConsensusCreateTopicTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='memo', full_name='proto.ConsensusCreateTopicTransactionBody.memo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adminKey', full_name='proto.ConsensusCreateTopicTransactionBody.adminKey', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submitKey', full_name='proto.ConsensusCreateTopicTransactionBody.submitKey', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autoRenewPeriod', full_name='proto.ConsensusCreateTopicTransactionBody.autoRenewPeriod', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autoRenewAccount', full_name='proto.ConsensusCreateTopicTransactionBody.autoRenewAccount', index=4,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=75,
  serialized_end=273,
)

_CONSENSUSCREATETOPICTRANSACTIONBODY.fields_by_name['adminKey'].message_type = basic__types__pb2._KEY
_CONSENSUSCREATETOPICTRANSACTIONBODY.fields_by_name['submitKey'].message_type = basic__types__pb2._KEY
_CONSENSUSCREATETOPICTRANSACTIONBODY.fields_by_name['autoRenewPeriod'].message_type = duration__pb2._DURATION
_CONSENSUSCREATETOPICTRANSACTIONBODY.fields_by_name['autoRenewAccount'].message_type = basic__types__pb2._ACCOUNTID
DESCRIPTOR.message_types_by_name['ConsensusCreateTopicTransactionBody'] = _CONSENSUSCREATETOPICTRANSACTIONBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConsensusCreateTopicTransactionBody = _reflection.GeneratedProtocolMessageType('ConsensusCreateTopicTransactionBody', (_message.Message,), {
  'DESCRIPTOR' : _CONSENSUSCREATETOPICTRANSACTIONBODY,
  '__module__' : 'consensus_create_topic_pb2'
  # @@protoc_insertion_point(class_scope:proto.ConsensusCreateTopicTransactionBody)
  })
_sym_db.RegisterMessage(ConsensusCreateTopicTransactionBody)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)