# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/resources/keyword_plan_ad_group_keyword.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import keyword_match_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_keyword__match__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/resources/keyword_plan_ad_group_keyword.proto',
  package='google.ads.googleads.v5.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v5.resourcesB\036KeywordPlanAdGroupKeywordProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V5.Resources\312\002!Google\\Ads\\GoogleAds\\V5\\Resources\352\002%Google::Ads::GoogleAds::V5::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nKgoogle/ads/googleads_v5/proto/resources/keyword_plan_ad_group_keyword.proto\x12!google.ads.googleads.v5.resources\x1a<google/ads/googleads_v5/proto/enums/keyword_match_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\x85\x05\n\x19KeywordPlanAdGroupKeyword\x12Q\n\rresource_name\x18\x01 \x01(\tB:\xe0\x41\x05\xfa\x41\x34\n2googleads.googleapis.com/KeywordPlanAdGroupKeyword\x12m\n\x15keyword_plan_ad_group\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB0\xfa\x41-\n+googleads.googleapis.com/KeywordPlanAdGroup\x12,\n\x02id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12*\n\x04text\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12X\n\nmatch_type\x18\x05 \x01(\x0e\x32\x44.google.ads.googleads.v5.enums.KeywordMatchTypeEnum.KeywordMatchType\x12\x33\n\x0e\x63pc_bid_micros\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x08negative\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x03\xe0\x41\x05:\x89\x01\xea\x41\x85\x01\n2googleads.googleapis.com/KeywordPlanAdGroupKeyword\x12Ocustomers/{customer}/keywordPlanAdGroupKeywords/{keyword_plan_ad_group_keyword}B\x8b\x02\n%com.google.ads.googleads.v5.resourcesB\x1eKeywordPlanAdGroupKeywordProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V5.Resources\xca\x02!Google\\Ads\\GoogleAds\\V5\\Resources\xea\x02%Google::Ads::GoogleAds::V5::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_keyword__match__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_KEYWORDPLANADGROUPKEYWORD = _descriptor.Descriptor(
  name='KeywordPlanAdGroupKeyword',
  full_name='google.ads.googleads.v5.resources.KeywordPlanAdGroupKeyword',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.resources.KeywordPlanAdGroupKeyword.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A4\n2googleads.googleapis.com/KeywordPlanAdGroupKeyword', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyword_plan_ad_group', full_name='google.ads.googleads.v5.resources.KeywordPlanAdGroupKeyword.keyword_plan_ad_group', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A-\n+googleads.googleapis.com/KeywordPlanAdGroup', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v5.resources.KeywordPlanAdGroupKeyword.id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='google.ads.googleads.v5.resources.KeywordPlanAdGroupKeyword.text', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='match_type', full_name='google.ads.googleads.v5.resources.KeywordPlanAdGroupKeyword.match_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpc_bid_micros', full_name='google.ads.googleads.v5.resources.KeywordPlanAdGroupKeyword.cpc_bid_micros', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='negative', full_name='google.ads.googleads.v5.resources.KeywordPlanAdGroupKeyword.negative', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A\205\001\n2googleads.googleapis.com/KeywordPlanAdGroupKeyword\022Ocustomers/{customer}/keywordPlanAdGroupKeywords/{keyword_plan_ad_group_keyword}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=944,
)

_KEYWORDPLANADGROUPKEYWORD.fields_by_name['keyword_plan_ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANADGROUPKEYWORD.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANADGROUPKEYWORD.fields_by_name['text'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANADGROUPKEYWORD.fields_by_name['match_type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_keyword__match__type__pb2._KEYWORDMATCHTYPEENUM_KEYWORDMATCHTYPE
_KEYWORDPLANADGROUPKEYWORD.fields_by_name['cpc_bid_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANADGROUPKEYWORD.fields_by_name['negative'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['KeywordPlanAdGroupKeyword'] = _KEYWORDPLANADGROUPKEYWORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanAdGroupKeyword = _reflection.GeneratedProtocolMessageType('KeywordPlanAdGroupKeyword', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANADGROUPKEYWORD,
  '__module__' : 'google.ads.googleads_v5.proto.resources.keyword_plan_ad_group_keyword_pb2'
  ,
  '__doc__': """A Keyword Plan ad group keyword. Max number of keyword plan keywords
  per plan: 10000.
  
  Attributes:
      resource_name:
          Immutable. The resource name of the Keyword Plan ad group
          keyword. KeywordPlanAdGroupKeyword resource names have the
          form:  ``customers/{customer_id}/keywordPlanAdGroupKeywords/{k
          p_ad_group_keyword_id}``
      keyword_plan_ad_group:
          The Keyword Plan ad group to which this keyword belongs.
      id:
          Output only. The ID of the Keyword Plan keyword.
      text:
          The keyword text.
      match_type:
          The keyword match type.
      cpc_bid_micros:
          A keyword level max cpc bid in micros (e.g. $1 = 1mm). The
          currency is the same as the account currency code. This will
          override any CPC bid set at the keyword plan ad group level.
          Not applicable for negative keywords. (negative = true) This
          field is Optional.
      negative:
          Immutable. If true, the keyword is negative.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.resources.KeywordPlanAdGroupKeyword)
  })
_sym_db.RegisterMessage(KeywordPlanAdGroupKeyword)


DESCRIPTOR._options = None
_KEYWORDPLANADGROUPKEYWORD.fields_by_name['resource_name']._options = None
_KEYWORDPLANADGROUPKEYWORD.fields_by_name['keyword_plan_ad_group']._options = None
_KEYWORDPLANADGROUPKEYWORD.fields_by_name['id']._options = None
_KEYWORDPLANADGROUPKEYWORD.fields_by_name['negative']._options = None
_KEYWORDPLANADGROUPKEYWORD._options = None
# @@protoc_insertion_point(module_scope)
