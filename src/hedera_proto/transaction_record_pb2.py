# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction_record.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import timestamp_pb2 as timestamp__pb2
import basic_types_pb2 as basic__types__pb2
import custom_fees_pb2 as custom__fees__pb2
import transaction_receipt_pb2 as transaction__receipt__pb2
import crypto_transfer_pb2 as crypto__transfer__pb2
import contract_call_local_pb2 as contract__call__local__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction_record.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18transaction_record.proto\x12\x05proto\x1a\x0ftimestamp.proto\x1a\x11\x62\x61sic_types.proto\x1a\x11\x63ustom_fees.proto\x1a\x19transaction_receipt.proto\x1a\x15\x63rypto_transfer.proto\x1a\x19\x63ontract_call_local.proto\"\xdd\x04\n\x11TransactionRecord\x12*\n\x07receipt\x18\x01 \x01(\x0b\x32\x19.proto.TransactionReceipt\x12\x17\n\x0ftransactionHash\x18\x02 \x01(\x0c\x12,\n\x12\x63onsensusTimestamp\x18\x03 \x01(\x0b\x32\x10.proto.Timestamp\x12+\n\rtransactionID\x18\x04 \x01(\x0b\x32\x14.proto.TransactionID\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x16\n\x0etransactionFee\x18\x06 \x01(\x04\x12;\n\x12\x63ontractCallResult\x18\x07 \x01(\x0b\x32\x1d.proto.ContractFunctionResultH\x00\x12=\n\x14\x63ontractCreateResult\x18\x08 \x01(\x0b\x32\x1d.proto.ContractFunctionResultH\x00\x12)\n\x0ctransferList\x18\n \x01(\x0b\x32\x13.proto.TransferList\x12\x34\n\x12tokenTransferLists\x18\x0b \x03(\x0b\x32\x18.proto.TokenTransferList\x12&\n\x0bscheduleRef\x18\x0c \x01(\x0b\x32\x11.proto.ScheduleID\x12\x36\n\x14\x61ssessed_custom_fees\x18\r \x03(\x0b\x32\x18.proto.AssessedCustomFee\x12=\n\x1c\x61utomatic_token_associations\x18\x0e \x03(\x0b\x32\x17.proto.TokenAssociationB\x06\n\x04\x62odyB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[timestamp__pb2.DESCRIPTOR,basic__types__pb2.DESCRIPTOR,custom__fees__pb2.DESCRIPTOR,transaction__receipt__pb2.DESCRIPTOR,crypto__transfer__pb2.DESCRIPTOR,contract__call__local__pb2.DESCRIPTOR,])




_TRANSACTIONRECORD = _descriptor.Descriptor(
  name='TransactionRecord',
  full_name='proto.TransactionRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='receipt', full_name='proto.TransactionRecord.receipt', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionHash', full_name='proto.TransactionRecord.transactionHash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consensusTimestamp', full_name='proto.TransactionRecord.consensusTimestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionID', full_name='proto.TransactionRecord.transactionID', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memo', full_name='proto.TransactionRecord.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionFee', full_name='proto.TransactionRecord.transactionFee', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractCallResult', full_name='proto.TransactionRecord.contractCallResult', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractCreateResult', full_name='proto.TransactionRecord.contractCreateResult', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transferList', full_name='proto.TransactionRecord.transferList', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokenTransferLists', full_name='proto.TransactionRecord.tokenTransferLists', index=9,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scheduleRef', full_name='proto.TransactionRecord.scheduleRef', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assessed_custom_fees', full_name='proto.TransactionRecord.assessed_custom_fees', index=11,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='automatic_token_associations', full_name='proto.TransactionRecord.automatic_token_associations', index=12,
      number=14, type=11, cpp_type=10, label=3,
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
    _descriptor.OneofDescriptor(
      name='body', full_name='proto.TransactionRecord.body',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=168,
  serialized_end=773,
)

_TRANSACTIONRECORD.fields_by_name['receipt'].message_type = transaction__receipt__pb2._TRANSACTIONRECEIPT
_TRANSACTIONRECORD.fields_by_name['consensusTimestamp'].message_type = timestamp__pb2._TIMESTAMP
_TRANSACTIONRECORD.fields_by_name['transactionID'].message_type = basic__types__pb2._TRANSACTIONID
_TRANSACTIONRECORD.fields_by_name['contractCallResult'].message_type = contract__call__local__pb2._CONTRACTFUNCTIONRESULT
_TRANSACTIONRECORD.fields_by_name['contractCreateResult'].message_type = contract__call__local__pb2._CONTRACTFUNCTIONRESULT
_TRANSACTIONRECORD.fields_by_name['transferList'].message_type = basic__types__pb2._TRANSFERLIST
_TRANSACTIONRECORD.fields_by_name['tokenTransferLists'].message_type = basic__types__pb2._TOKENTRANSFERLIST
_TRANSACTIONRECORD.fields_by_name['scheduleRef'].message_type = basic__types__pb2._SCHEDULEID
_TRANSACTIONRECORD.fields_by_name['assessed_custom_fees'].message_type = custom__fees__pb2._ASSESSEDCUSTOMFEE
_TRANSACTIONRECORD.fields_by_name['automatic_token_associations'].message_type = basic__types__pb2._TOKENASSOCIATION
_TRANSACTIONRECORD.oneofs_by_name['body'].fields.append(
  _TRANSACTIONRECORD.fields_by_name['contractCallResult'])
_TRANSACTIONRECORD.fields_by_name['contractCallResult'].containing_oneof = _TRANSACTIONRECORD.oneofs_by_name['body']
_TRANSACTIONRECORD.oneofs_by_name['body'].fields.append(
  _TRANSACTIONRECORD.fields_by_name['contractCreateResult'])
_TRANSACTIONRECORD.fields_by_name['contractCreateResult'].containing_oneof = _TRANSACTIONRECORD.oneofs_by_name['body']
DESCRIPTOR.message_types_by_name['TransactionRecord'] = _TRANSACTIONRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionRecord = _reflection.GeneratedProtocolMessageType('TransactionRecord', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONRECORD,
  '__module__' : 'transaction_record_pb2'
  # @@protoc_insertion_point(class_scope:proto.TransactionRecord)
  })
_sym_db.RegisterMessage(TransactionRecord)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)