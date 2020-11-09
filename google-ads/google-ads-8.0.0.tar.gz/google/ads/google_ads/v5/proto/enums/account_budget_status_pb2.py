# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/enums/account_budget_status.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/enums/account_budget_status.proto',
  package='google.ads.googleads.v5.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v5.enumsB\030AccountBudgetStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V5.Enums\312\002\035Google\\Ads\\GoogleAds\\V5\\Enums\352\002!Google::Ads::GoogleAds::V5::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?google/ads/googleads_v5/proto/enums/account_budget_status.proto\x12\x1dgoogle.ads.googleads.v5.enums\x1a\x1cgoogle/api/annotations.proto\"x\n\x17\x41\x63\x63ountBudgetStatusEnum\"]\n\x13\x41\x63\x63ountBudgetStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0c\n\x08\x41PPROVED\x10\x03\x12\r\n\tCANCELLED\x10\x04\x42\xed\x01\n!com.google.ads.googleads.v5.enumsB\x18\x41\x63\x63ountBudgetStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V5.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V5\\Enums\xea\x02!Google::Ads::GoogleAds::V5::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ACCOUNTBUDGETSTATUSENUM_ACCOUNTBUDGETSTATUS = _descriptor.EnumDescriptor(
  name='AccountBudgetStatus',
  full_name='google.ads.googleads.v5.enums.AccountBudgetStatusEnum.AccountBudgetStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPROVED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=155,
  serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTBUDGETSTATUSENUM_ACCOUNTBUDGETSTATUS)


_ACCOUNTBUDGETSTATUSENUM = _descriptor.Descriptor(
  name='AccountBudgetStatusEnum',
  full_name='google.ads.googleads.v5.enums.AccountBudgetStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCOUNTBUDGETSTATUSENUM_ACCOUNTBUDGETSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=248,
)

_ACCOUNTBUDGETSTATUSENUM_ACCOUNTBUDGETSTATUS.containing_type = _ACCOUNTBUDGETSTATUSENUM
DESCRIPTOR.message_types_by_name['AccountBudgetStatusEnum'] = _ACCOUNTBUDGETSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountBudgetStatusEnum = _reflection.GeneratedProtocolMessageType('AccountBudgetStatusEnum', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTBUDGETSTATUSENUM,
  '__module__' : 'google.ads.googleads_v5.proto.enums.account_budget_status_pb2'
  ,
  '__doc__': """Message describing AccountBudget statuses.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.enums.AccountBudgetStatusEnum)
  })
_sym_db.RegisterMessage(AccountBudgetStatusEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
