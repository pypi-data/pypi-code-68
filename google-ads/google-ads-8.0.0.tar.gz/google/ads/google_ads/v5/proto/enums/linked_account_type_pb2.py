# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/enums/linked_account_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/enums/linked_account_type.proto',
  package='google.ads.googleads.v5.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v5.enumsB\026LinkedAccountTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V5.Enums\312\002\035Google\\Ads\\GoogleAds\\V5\\Enums\352\002!Google::Ads::GoogleAds::V5::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=google/ads/googleads_v5/proto/enums/linked_account_type.proto\x12\x1dgoogle.ads.googleads.v5.enums\x1a\x1cgoogle/api/annotations.proto\"\x8b\x01\n\x15LinkedAccountTypeEnum\"r\n\x11LinkedAccountType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1d\n\x19THIRD_PARTY_APP_ANALYTICS\x10\x02\x12\x10\n\x0c\x44\x41TA_PARTNER\x10\x03\x12\x0e\n\nGOOGLE_ADS\x10\x04\x42\xeb\x01\n!com.google.ads.googleads.v5.enumsB\x16LinkedAccountTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V5.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V5\\Enums\xea\x02!Google::Ads::GoogleAds::V5::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_LINKEDACCOUNTTYPEENUM_LINKEDACCOUNTTYPE = _descriptor.EnumDescriptor(
  name='LinkedAccountType',
  full_name='google.ads.googleads.v5.enums.LinkedAccountTypeEnum.LinkedAccountType',
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
      name='THIRD_PARTY_APP_ANALYTICS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATA_PARTNER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_ADS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=152,
  serialized_end=266,
)
_sym_db.RegisterEnumDescriptor(_LINKEDACCOUNTTYPEENUM_LINKEDACCOUNTTYPE)


_LINKEDACCOUNTTYPEENUM = _descriptor.Descriptor(
  name='LinkedAccountTypeEnum',
  full_name='google.ads.googleads.v5.enums.LinkedAccountTypeEnum',
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
    _LINKEDACCOUNTTYPEENUM_LINKEDACCOUNTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=266,
)

_LINKEDACCOUNTTYPEENUM_LINKEDACCOUNTTYPE.containing_type = _LINKEDACCOUNTTYPEENUM
DESCRIPTOR.message_types_by_name['LinkedAccountTypeEnum'] = _LINKEDACCOUNTTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LinkedAccountTypeEnum = _reflection.GeneratedProtocolMessageType('LinkedAccountTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _LINKEDACCOUNTTYPEENUM,
  '__module__' : 'google.ads.googleads_v5.proto.enums.linked_account_type_pb2'
  ,
  '__doc__': """Container for enum describing different types of Linked accounts.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.enums.LinkedAccountTypeEnum)
  })
_sym_db.RegisterMessage(LinkedAccountTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
