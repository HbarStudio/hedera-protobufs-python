# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto_get_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import timestamp_pb2 as timestamp__pb2
import duration_pb2 as duration__pb2
import basic_types_pb2 as basic__types__pb2
import query_header_pb2 as query__header__pb2
import response_header_pb2 as response__header__pb2
import crypto_add_live_hash_pb2 as crypto__add__live__hash__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='crypto_get_info.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x63rypto_get_info.proto\x12\x05proto\x1a\x0ftimestamp.proto\x1a\x0e\x64uration.proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\x1a\x1a\x63rypto_add_live_hash.proto\"]\n\x12\x43ryptoGetInfoQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12#\n\taccountID\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\"\xc4\x05\n\x15\x43ryptoGetInfoResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12=\n\x0b\x61\x63\x63ountInfo\x18\x02 \x01(\x0b\x32(.proto.CryptoGetInfoResponse.AccountInfo\x1a\xc4\x04\n\x0b\x41\x63\x63ountInfo\x12#\n\taccountID\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12\x19\n\x11\x63ontractAccountID\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65leted\x18\x03 \x01(\x08\x12(\n\x0eproxyAccountID\x18\x04 \x01(\x0b\x32\x10.proto.AccountID\x12\x15\n\rproxyReceived\x18\x06 \x01(\x03\x12\x17\n\x03key\x18\x07 \x01(\x0b\x32\n.proto.Key\x12\x0f\n\x07\x62\x61lance\x18\x08 \x01(\x04\x12\'\n\x1bgenerateSendRecordThreshold\x18\t \x01(\x04\x42\x02\x18\x01\x12*\n\x1egenerateReceiveRecordThreshold\x18\n \x01(\x04\x42\x02\x18\x01\x12\x1b\n\x13receiverSigRequired\x18\x0b \x01(\x08\x12(\n\x0e\x65xpirationTime\x18\x0c \x01(\x0b\x32\x10.proto.Timestamp\x12(\n\x0f\x61utoRenewPeriod\x18\r \x01(\x0b\x32\x0f.proto.Duration\x12#\n\nliveHashes\x18\x0e \x03(\x0b\x32\x0f.proto.LiveHash\x12\x34\n\x12tokenRelationships\x18\x0f \x03(\x0b\x32\x18.proto.TokenRelationship\x12\x0c\n\x04memo\x18\x10 \x01(\t\x12\x11\n\townedNfts\x18\x11 \x01(\x03\x12(\n max_automatic_token_associations\x18\x12 \x01(\x05\x12\r\n\x05\x61lias\x18\x13 \x01(\x0c\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[timestamp__pb2.DESCRIPTOR,duration__pb2.DESCRIPTOR,basic__types__pb2.DESCRIPTOR,query__header__pb2.DESCRIPTOR,response__header__pb2.DESCRIPTOR,crypto__add__live__hash__pb2.DESCRIPTOR,])




_CRYPTOGETINFOQUERY = _descriptor.Descriptor(
  name='CryptoGetInfoQuery',
  full_name='proto.CryptoGetInfoQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.CryptoGetInfoQuery.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountID', full_name='proto.CryptoGetInfoQuery.accountID', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=155,
  serialized_end=248,
)


_CRYPTOGETINFORESPONSE_ACCOUNTINFO = _descriptor.Descriptor(
  name='AccountInfo',
  full_name='proto.CryptoGetInfoResponse.AccountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountID', full_name='proto.CryptoGetInfoResponse.AccountInfo.accountID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractAccountID', full_name='proto.CryptoGetInfoResponse.AccountInfo.contractAccountID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='proto.CryptoGetInfoResponse.AccountInfo.deleted', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxyAccountID', full_name='proto.CryptoGetInfoResponse.AccountInfo.proxyAccountID', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxyReceived', full_name='proto.CryptoGetInfoResponse.AccountInfo.proxyReceived', index=4,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.CryptoGetInfoResponse.AccountInfo.key', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='balance', full_name='proto.CryptoGetInfoResponse.AccountInfo.balance', index=6,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generateSendRecordThreshold', full_name='proto.CryptoGetInfoResponse.AccountInfo.generateSendRecordThreshold', index=7,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generateReceiveRecordThreshold', full_name='proto.CryptoGetInfoResponse.AccountInfo.generateReceiveRecordThreshold', index=8,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiverSigRequired', full_name='proto.CryptoGetInfoResponse.AccountInfo.receiverSigRequired', index=9,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expirationTime', full_name='proto.CryptoGetInfoResponse.AccountInfo.expirationTime', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autoRenewPeriod', full_name='proto.CryptoGetInfoResponse.AccountInfo.autoRenewPeriod', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='liveHashes', full_name='proto.CryptoGetInfoResponse.AccountInfo.liveHashes', index=12,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokenRelationships', full_name='proto.CryptoGetInfoResponse.AccountInfo.tokenRelationships', index=13,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memo', full_name='proto.CryptoGetInfoResponse.AccountInfo.memo', index=14,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ownedNfts', full_name='proto.CryptoGetInfoResponse.AccountInfo.ownedNfts', index=15,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_automatic_token_associations', full_name='proto.CryptoGetInfoResponse.AccountInfo.max_automatic_token_associations', index=16,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alias', full_name='proto.CryptoGetInfoResponse.AccountInfo.alias', index=17,
      number=19, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=379,
  serialized_end=959,
)

_CRYPTOGETINFORESPONSE = _descriptor.Descriptor(
  name='CryptoGetInfoResponse',
  full_name='proto.CryptoGetInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.CryptoGetInfoResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountInfo', full_name='proto.CryptoGetInfoResponse.accountInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CRYPTOGETINFORESPONSE_ACCOUNTINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=959,
)

_CRYPTOGETINFOQUERY.fields_by_name['header'].message_type = query__header__pb2._QUERYHEADER
_CRYPTOGETINFOQUERY.fields_by_name['accountID'].message_type = basic__types__pb2._ACCOUNTID
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.fields_by_name['accountID'].message_type = basic__types__pb2._ACCOUNTID
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.fields_by_name['proxyAccountID'].message_type = basic__types__pb2._ACCOUNTID
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.fields_by_name['key'].message_type = basic__types__pb2._KEY
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.fields_by_name['expirationTime'].message_type = timestamp__pb2._TIMESTAMP
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.fields_by_name['autoRenewPeriod'].message_type = duration__pb2._DURATION
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.fields_by_name['liveHashes'].message_type = crypto__add__live__hash__pb2._LIVEHASH
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.fields_by_name['tokenRelationships'].message_type = basic__types__pb2._TOKENRELATIONSHIP
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.containing_type = _CRYPTOGETINFORESPONSE
_CRYPTOGETINFORESPONSE.fields_by_name['header'].message_type = response__header__pb2._RESPONSEHEADER
_CRYPTOGETINFORESPONSE.fields_by_name['accountInfo'].message_type = _CRYPTOGETINFORESPONSE_ACCOUNTINFO
DESCRIPTOR.message_types_by_name['CryptoGetInfoQuery'] = _CRYPTOGETINFOQUERY
DESCRIPTOR.message_types_by_name['CryptoGetInfoResponse'] = _CRYPTOGETINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CryptoGetInfoQuery = _reflection.GeneratedProtocolMessageType('CryptoGetInfoQuery', (_message.Message,), {
  'DESCRIPTOR' : _CRYPTOGETINFOQUERY,
  '__module__' : 'crypto_get_info_pb2'
  # @@protoc_insertion_point(class_scope:proto.CryptoGetInfoQuery)
  })
_sym_db.RegisterMessage(CryptoGetInfoQuery)

CryptoGetInfoResponse = _reflection.GeneratedProtocolMessageType('CryptoGetInfoResponse', (_message.Message,), {

  'AccountInfo' : _reflection.GeneratedProtocolMessageType('AccountInfo', (_message.Message,), {
    'DESCRIPTOR' : _CRYPTOGETINFORESPONSE_ACCOUNTINFO,
    '__module__' : 'crypto_get_info_pb2'
    # @@protoc_insertion_point(class_scope:proto.CryptoGetInfoResponse.AccountInfo)
    })
  ,
  'DESCRIPTOR' : _CRYPTOGETINFORESPONSE,
  '__module__' : 'crypto_get_info_pb2'
  # @@protoc_insertion_point(class_scope:proto.CryptoGetInfoResponse)
  })
_sym_db.RegisterMessage(CryptoGetInfoResponse)
_sym_db.RegisterMessage(CryptoGetInfoResponse.AccountInfo)


DESCRIPTOR._options = None
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.fields_by_name['generateSendRecordThreshold']._options = None
_CRYPTOGETINFORESPONSE_ACCOUNTINFO.fields_by_name['generateReceiveRecordThreshold']._options = None
# @@protoc_insertion_point(module_scope)
