# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/enums/keyword_plan_competition_level.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/enums/keyword_plan_competition_level.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB KeywordPlanCompetitionLevelProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nHgoogle/ads/googleads_v6/proto/enums/keyword_plan_competition_level.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"}\n\x1fKeywordPlanCompetitionLevelEnum\"Z\n\x1bKeywordPlanCompetitionLevel\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03LOW\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x08\n\x04HIGH\x10\x04\x42\xf5\x01\n!com.google.ads.googleads.v6.enumsB KeywordPlanCompetitionLevelProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_KEYWORDPLANCOMPETITIONLEVELENUM_KEYWORDPLANCOMPETITIONLEVEL = _descriptor.EnumDescriptor(
  name='KeywordPlanCompetitionLevel',
  full_name='google.ads.googleads.v6.enums.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel',
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
      name='LOW', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=172,
  serialized_end=262,
)
_sym_db.RegisterEnumDescriptor(_KEYWORDPLANCOMPETITIONLEVELENUM_KEYWORDPLANCOMPETITIONLEVEL)


_KEYWORDPLANCOMPETITIONLEVELENUM = _descriptor.Descriptor(
  name='KeywordPlanCompetitionLevelEnum',
  full_name='google.ads.googleads.v6.enums.KeywordPlanCompetitionLevelEnum',
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
    _KEYWORDPLANCOMPETITIONLEVELENUM_KEYWORDPLANCOMPETITIONLEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=262,
)

_KEYWORDPLANCOMPETITIONLEVELENUM_KEYWORDPLANCOMPETITIONLEVEL.containing_type = _KEYWORDPLANCOMPETITIONLEVELENUM
DESCRIPTOR.message_types_by_name['KeywordPlanCompetitionLevelEnum'] = _KEYWORDPLANCOMPETITIONLEVELENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanCompetitionLevelEnum = _reflection.GeneratedProtocolMessageType('KeywordPlanCompetitionLevelEnum', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANCOMPETITIONLEVELENUM,
  '__module__' : 'google.ads.googleads_v6.proto.enums.keyword_plan_competition_level_pb2'
  ,
  '__doc__': """Container for enumeration of keyword competition levels. The
  competition level indicates how competitive ad placement is for a
  keyword and is determined by the number of advertisers bidding on that
  keyword relative to all keywords across Google. The competition level
  can depend on the location and Search Network targeting options you've
  selected.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.KeywordPlanCompetitionLevelEnum)
  })
_sym_db.RegisterMessage(KeywordPlanCompetitionLevelEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
