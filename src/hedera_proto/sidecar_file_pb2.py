# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sidecar_file.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2
import timestamp_pb2 as timestamp__pb2
import contract_state_change_pb2 as contract__state__change__pb2
import contract_action_pb2 as contract__action__pb2
import contract_bytecode_pb2 as contract__bytecode__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12sidecar_file.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0ftimestamp.proto\x1a\x1b\x63ontract_state_change.proto\x1a\x15\x63ontract_action.proto\x1a\x17\x63ontract_bytecode.proto\"G\n\x0bSidecarFile\x12\x38\n\x0fsidecar_records\x18\x01 \x03(\x0b\x32\x1f.proto.TransactionSidecarRecord\"\xfd\x01\n\x18TransactionSidecarRecord\x12-\n\x13\x63onsensus_timestamp\x18\x01 \x01(\x0b\x32\x10.proto.Timestamp\x12\x11\n\tmigration\x18\x02 \x01(\x08\x12\x34\n\rstate_changes\x18\x03 \x01(\x0b\x32\x1b.proto.ContractStateChangesH\x00\x12)\n\x07\x61\x63tions\x18\x04 \x01(\x0b\x32\x16.proto.ContractActionsH\x00\x12+\n\x08\x62ytecode\x18\x05 \x01(\x0b\x32\x17.proto.ContractBytecodeH\x00\x42\x11\n\x0fsidecar_recordsB$\n com.hedera.services.stream.protoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sidecar_file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.hedera.services.stream.protoP\001'
  _globals['_SIDECARFILE']._serialized_start=142
  _globals['_SIDECARFILE']._serialized_end=213
  _globals['_TRANSACTIONSIDECARRECORD']._serialized_start=216
  _globals['_TRANSACTIONSIDECARRECORD']._serialized_end=469
# @@protoc_insertion_point(module_scope)
