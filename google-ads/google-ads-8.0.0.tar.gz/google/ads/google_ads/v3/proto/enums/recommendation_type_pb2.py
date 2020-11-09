# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/recommendation_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/enums/recommendation_type.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\027RecommendationTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\n=google/ads/googleads_v3/proto/enums/recommendation_type.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"\x92\x03\n\x16RecommendationTypeEnum\"\xf7\x02\n\x12RecommendationType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x13\n\x0f\x43\x41MPAIGN_BUDGET\x10\x02\x12\x0b\n\x07KEYWORD\x10\x03\x12\x0b\n\x07TEXT_AD\x10\x04\x12\x15\n\x11TARGET_CPA_OPT_IN\x10\x05\x12\x1f\n\x1bMAXIMIZE_CONVERSIONS_OPT_IN\x10\x06\x12\x17\n\x13\x45NHANCED_CPC_OPT_IN\x10\x07\x12\x1a\n\x16SEARCH_PARTNERS_OPT_IN\x10\x08\x12\x1a\n\x16MAXIMIZE_CLICKS_OPT_IN\x10\t\x12\x18\n\x14OPTIMIZE_AD_ROTATION\x10\n\x12\x15\n\x11\x43\x41LLOUT_EXTENSION\x10\x0b\x12\x16\n\x12SITELINK_EXTENSION\x10\x0c\x12\x12\n\x0e\x43\x41LL_EXTENSION\x10\r\x12\x16\n\x12KEYWORD_MATCH_TYPE\x10\x0e\x12\x16\n\x12MOVE_UNUSED_BUDGET\x10\x0f\x42\xec\x01\n!com.google.ads.googleads.v3.enumsB\x17RecommendationTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_RECOMMENDATIONTYPEENUM_RECOMMENDATIONTYPE = _descriptor.EnumDescriptor(
  name='RecommendationType',
  full_name='google.ads.googleads.v3.enums.RecommendationTypeEnum.RecommendationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_BUDGET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYWORD', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_AD', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_CPA_OPT_IN', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE_CONVERSIONS_OPT_IN', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENHANCED_CPC_OPT_IN', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_PARTNERS_OPT_IN', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE_CLICKS_OPT_IN', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPTIMIZE_AD_ROTATION', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALLOUT_EXTENSION', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SITELINK_EXTENSION', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_EXTENSION', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYWORD_MATCH_TYPE', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_UNUSED_BUDGET', index=15, number=15,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=529,
)
_sym_db.RegisterEnumDescriptor(_RECOMMENDATIONTYPEENUM_RECOMMENDATIONTYPE)


_RECOMMENDATIONTYPEENUM = _descriptor.Descriptor(
  name='RecommendationTypeEnum',
  full_name='google.ads.googleads.v3.enums.RecommendationTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECOMMENDATIONTYPEENUM_RECOMMENDATIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=529,
)

_RECOMMENDATIONTYPEENUM_RECOMMENDATIONTYPE.containing_type = _RECOMMENDATIONTYPEENUM
DESCRIPTOR.message_types_by_name['RecommendationTypeEnum'] = _RECOMMENDATIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecommendationTypeEnum = _reflection.GeneratedProtocolMessageType('RecommendationTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _RECOMMENDATIONTYPEENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.recommendation_type_pb2'
  ,
  __doc__ = """Container for enum describing types of recommendations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.RecommendationTypeEnum)
  ))
_sym_db.RegisterMessage(RecommendationTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
