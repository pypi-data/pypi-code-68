# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/services/keyword_plan_idea_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.common import keyword_plan_common_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_keyword__plan__common__pb2
from google.ads.google_ads.v5.proto.enums import keyword_plan_network_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_keyword__plan__network__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/services/keyword_plan_idea_service.proto',
  package='google.ads.googleads.v5.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v5.servicesB\033KeywordPlanIdeaServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V5.Services\312\002 Google\\Ads\\GoogleAds\\V5\\Services\352\002$Google::Ads::GoogleAds::V5::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nFgoogle/ads/googleads_v5/proto/services/keyword_plan_idea_service.proto\x12 google.ads.googleads.v5.services\x1a>google/ads/googleads_v5/proto/common/keyword_plan_common.proto\x1a>google/ads/googleads_v5/proto/enums/keyword_plan_network.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/api/client.proto\"\xf6\x04\n\x1bGenerateKeywordIdeasRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x33\n\x08language\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x02\x12:\n\x14geo_target_constants\x18\x08 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1e\n\x16include_adult_keywords\x18\n \x01(\x08\x12\x12\n\npage_token\x18\x0c \x01(\t\x12\x11\n\tpage_size\x18\r \x01(\x05\x12\x66\n\x14keyword_plan_network\x18\t \x01(\x0e\x32H.google.ads.googleads.v5.enums.KeywordPlanNetworkEnum.KeywordPlanNetwork\x12S\n\x14keyword_and_url_seed\x18\x02 \x01(\x0b\x32\x33.google.ads.googleads.v5.services.KeywordAndUrlSeedH\x00\x12\x45\n\x0ckeyword_seed\x18\x03 \x01(\x0b\x32-.google.ads.googleads.v5.services.KeywordSeedH\x00\x12=\n\x08url_seed\x18\x05 \x01(\x0b\x32).google.ads.googleads.v5.services.UrlSeedH\x00\x12?\n\tsite_seed\x18\x0b \x01(\x0b\x32*.google.ads.googleads.v5.services.SiteSeedH\x00\x42\x06\n\x04seed\"n\n\x11KeywordAndUrlSeed\x12)\n\x03url\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08keywords\x18\x02 \x03(\x0b\x32\x1c.google.protobuf.StringValue\"=\n\x0bKeywordSeed\x12.\n\x08keywords\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.StringValue\"6\n\x08SiteSeed\x12*\n\x04site\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"4\n\x07UrlSeed\x12)\n\x03url\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x98\x01\n\x1bGenerateKeywordIdeaResponse\x12L\n\x07results\x18\x01 \x03(\x0b\x32;.google.ads.googleads.v5.services.GenerateKeywordIdeaResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x03\"\xa3\x01\n\x19GenerateKeywordIdeaResult\x12*\n\x04text\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12Z\n\x14keyword_idea_metrics\x18\x03 \x01(\x0b\x32<.google.ads.googleads.v5.common.KeywordPlanHistoricalMetrics2\x8b\x02\n\x16KeywordPlanIdeaService\x12\xd3\x01\n\x14GenerateKeywordIdeas\x12=.google.ads.googleads.v5.services.GenerateKeywordIdeasRequest\x1a=.google.ads.googleads.v5.services.GenerateKeywordIdeaResponse\"=\x82\xd3\xe4\x93\x02\x37\"2/v5/customers/{customer_id=*}:generateKeywordIdeas:\x01*\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x82\x02\n$com.google.ads.googleads.v5.servicesB\x1bKeywordPlanIdeaServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V5.Services\xca\x02 Google\\Ads\\GoogleAds\\V5\\Services\xea\x02$Google::Ads::GoogleAds::V5::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_keyword__plan__common__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_keyword__plan__network__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_GENERATEKEYWORDIDEASREQUEST = _descriptor.Descriptor(
  name='GenerateKeywordIdeasRequest',
  full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.language', index=1,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geo_target_constants', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.geo_target_constants', index=2,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='include_adult_keywords', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.include_adult_keywords', index=3,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.page_token', index=4,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.page_size', index=5,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyword_plan_network', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.keyword_plan_network', index=6,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyword_and_url_seed', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.keyword_and_url_seed', index=7,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyword_seed', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.keyword_seed', index=8,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url_seed', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.url_seed', index=9,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='site_seed', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.site_seed', index=10,
      number=11, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='seed', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeasRequest.seed',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=357,
  serialized_end=987,
)


_KEYWORDANDURLSEED = _descriptor.Descriptor(
  name='KeywordAndUrlSeed',
  full_name='google.ads.googleads.v5.services.KeywordAndUrlSeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='google.ads.googleads.v5.services.KeywordAndUrlSeed.url', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keywords', full_name='google.ads.googleads.v5.services.KeywordAndUrlSeed.keywords', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  ],
  serialized_start=989,
  serialized_end=1099,
)


_KEYWORDSEED = _descriptor.Descriptor(
  name='KeywordSeed',
  full_name='google.ads.googleads.v5.services.KeywordSeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keywords', full_name='google.ads.googleads.v5.services.KeywordSeed.keywords', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  ],
  serialized_start=1101,
  serialized_end=1162,
)


_SITESEED = _descriptor.Descriptor(
  name='SiteSeed',
  full_name='google.ads.googleads.v5.services.SiteSeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='site', full_name='google.ads.googleads.v5.services.SiteSeed.site', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1164,
  serialized_end=1218,
)


_URLSEED = _descriptor.Descriptor(
  name='UrlSeed',
  full_name='google.ads.googleads.v5.services.UrlSeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='google.ads.googleads.v5.services.UrlSeed.url', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1220,
  serialized_end=1272,
)


_GENERATEKEYWORDIDEARESPONSE = _descriptor.Descriptor(
  name='GenerateKeywordIdeaResponse',
  full_name='google.ads.googleads.v5.services.GenerateKeywordIdeaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeaResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeaResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_size', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeaResponse.total_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1275,
  serialized_end=1427,
)


_GENERATEKEYWORDIDEARESULT = _descriptor.Descriptor(
  name='GenerateKeywordIdeaResult',
  full_name='google.ads.googleads.v5.services.GenerateKeywordIdeaResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeaResult.text', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyword_idea_metrics', full_name='google.ads.googleads.v5.services.GenerateKeywordIdeaResult.keyword_idea_metrics', index=1,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1430,
  serialized_end=1593,
)

_GENERATEKEYWORDIDEASREQUEST.fields_by_name['language'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['geo_target_constants'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['keyword_plan_network'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_keyword__plan__network__pb2._KEYWORDPLANNETWORKENUM_KEYWORDPLANNETWORK
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['keyword_and_url_seed'].message_type = _KEYWORDANDURLSEED
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['keyword_seed'].message_type = _KEYWORDSEED
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['url_seed'].message_type = _URLSEED
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['site_seed'].message_type = _SITESEED
_GENERATEKEYWORDIDEASREQUEST.oneofs_by_name['seed'].fields.append(
  _GENERATEKEYWORDIDEASREQUEST.fields_by_name['keyword_and_url_seed'])
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['keyword_and_url_seed'].containing_oneof = _GENERATEKEYWORDIDEASREQUEST.oneofs_by_name['seed']
_GENERATEKEYWORDIDEASREQUEST.oneofs_by_name['seed'].fields.append(
  _GENERATEKEYWORDIDEASREQUEST.fields_by_name['keyword_seed'])
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['keyword_seed'].containing_oneof = _GENERATEKEYWORDIDEASREQUEST.oneofs_by_name['seed']
_GENERATEKEYWORDIDEASREQUEST.oneofs_by_name['seed'].fields.append(
  _GENERATEKEYWORDIDEASREQUEST.fields_by_name['url_seed'])
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['url_seed'].containing_oneof = _GENERATEKEYWORDIDEASREQUEST.oneofs_by_name['seed']
_GENERATEKEYWORDIDEASREQUEST.oneofs_by_name['seed'].fields.append(
  _GENERATEKEYWORDIDEASREQUEST.fields_by_name['site_seed'])
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['site_seed'].containing_oneof = _GENERATEKEYWORDIDEASREQUEST.oneofs_by_name['seed']
_KEYWORDANDURLSEED.fields_by_name['url'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDANDURLSEED.fields_by_name['keywords'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDSEED.fields_by_name['keywords'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SITESEED.fields_by_name['site'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_URLSEED.fields_by_name['url'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_GENERATEKEYWORDIDEARESPONSE.fields_by_name['results'].message_type = _GENERATEKEYWORDIDEARESULT
_GENERATEKEYWORDIDEARESULT.fields_by_name['text'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_GENERATEKEYWORDIDEARESULT.fields_by_name['keyword_idea_metrics'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_keyword__plan__common__pb2._KEYWORDPLANHISTORICALMETRICS
DESCRIPTOR.message_types_by_name['GenerateKeywordIdeasRequest'] = _GENERATEKEYWORDIDEASREQUEST
DESCRIPTOR.message_types_by_name['KeywordAndUrlSeed'] = _KEYWORDANDURLSEED
DESCRIPTOR.message_types_by_name['KeywordSeed'] = _KEYWORDSEED
DESCRIPTOR.message_types_by_name['SiteSeed'] = _SITESEED
DESCRIPTOR.message_types_by_name['UrlSeed'] = _URLSEED
DESCRIPTOR.message_types_by_name['GenerateKeywordIdeaResponse'] = _GENERATEKEYWORDIDEARESPONSE
DESCRIPTOR.message_types_by_name['GenerateKeywordIdeaResult'] = _GENERATEKEYWORDIDEARESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateKeywordIdeasRequest = _reflection.GeneratedProtocolMessageType('GenerateKeywordIdeasRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYWORDIDEASREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.keyword_plan_idea_service_pb2'
  ,
  '__doc__': """Request message for [KeywordPlanIdeaService.GenerateKeywordIdeas][goog
  le.ads.googleads.v5.services.KeywordPlanIdeaService.GenerateKeywordIde
  as].
  
  Attributes:
      customer_id:
          The ID of the customer with the recommendation.
      language:
          Required. The resource name of the language to target.
          Required
      geo_target_constants:
          The resource names of the location to target. Max 10
      include_adult_keywords:
          If true, adult keywords will be included in response. The
          default value is false.
      page_token:
          Token of the page to retrieve. If not specified, the first
          page of results will be returned. To request next page of
          results use the value obtained from ``next_page_token`` in the
          previous response. The request fields must match across pages.
      page_size:
          Number of results to retrieve in a single page. A maximum of
          10,000 results may be returned, if the page\_size exceeds
          this, it is ignored. If unspecified, at most 10,000 results
          will be returned. The server may decide to further limit the
          number of returned resources. If the response contains fewer
          than 10,000 results it may not be assumed as last page of
          results.
      keyword_plan_network:
          Targeting network.
      seed:
          The type of seed to generate keyword ideas.
      keyword_and_url_seed:
          A Keyword and a specific Url to generate ideas from e.g. cars,
          www.example.com/cars.
      keyword_seed:
          A Keyword or phrase to generate ideas from, e.g. cars.
      url_seed:
          A specific url to generate ideas from, e.g.
          www.example.com/cars.
      site_seed:
          The site to generate ideas from, e.g. www.example.com.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.GenerateKeywordIdeasRequest)
  })
_sym_db.RegisterMessage(GenerateKeywordIdeasRequest)

KeywordAndUrlSeed = _reflection.GeneratedProtocolMessageType('KeywordAndUrlSeed', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDANDURLSEED,
  '__module__' : 'google.ads.googleads_v5.proto.services.keyword_plan_idea_service_pb2'
  ,
  '__doc__': """Keyword And Url Seed
  
  Attributes:
      url:
          The URL to crawl in order to generate keyword ideas.
      keywords:
          Requires at least one keyword.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.KeywordAndUrlSeed)
  })
_sym_db.RegisterMessage(KeywordAndUrlSeed)

KeywordSeed = _reflection.GeneratedProtocolMessageType('KeywordSeed', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDSEED,
  '__module__' : 'google.ads.googleads_v5.proto.services.keyword_plan_idea_service_pb2'
  ,
  '__doc__': """Keyword Seed
  
  Attributes:
      keywords:
          Requires at least one keyword.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.KeywordSeed)
  })
_sym_db.RegisterMessage(KeywordSeed)

SiteSeed = _reflection.GeneratedProtocolMessageType('SiteSeed', (_message.Message,), {
  'DESCRIPTOR' : _SITESEED,
  '__module__' : 'google.ads.googleads_v5.proto.services.keyword_plan_idea_service_pb2'
  ,
  '__doc__': """Site Seed
  
  Attributes:
      site:
          The domain name of the site. If the customer requesting the
          ideas doesn't own the site provided only public information is
          returned.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.SiteSeed)
  })
_sym_db.RegisterMessage(SiteSeed)

UrlSeed = _reflection.GeneratedProtocolMessageType('UrlSeed', (_message.Message,), {
  'DESCRIPTOR' : _URLSEED,
  '__module__' : 'google.ads.googleads_v5.proto.services.keyword_plan_idea_service_pb2'
  ,
  '__doc__': """Url Seed
  
  Attributes:
      url:
          The URL to crawl in order to generate keyword ideas.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.UrlSeed)
  })
_sym_db.RegisterMessage(UrlSeed)

GenerateKeywordIdeaResponse = _reflection.GeneratedProtocolMessageType('GenerateKeywordIdeaResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYWORDIDEARESPONSE,
  '__module__' : 'google.ads.googleads_v5.proto.services.keyword_plan_idea_service_pb2'
  ,
  '__doc__': """Response message for [KeywordPlanIdeaService.GenerateKeywordIdeas][goo
  gle.ads.googleads.v5.services.KeywordPlanIdeaService.GenerateKeywordId
  eas].
  
  Attributes:
      results:
          Results of generating keyword ideas.
      next_page_token:
          Pagination token used to retrieve the next page of results.
          Pass the content of this string as the ``page_token``
          attribute of the next request. ``next_page_token`` is not
          returned for the last page.
      total_size:
          Total number of results available.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.GenerateKeywordIdeaResponse)
  })
_sym_db.RegisterMessage(GenerateKeywordIdeaResponse)

GenerateKeywordIdeaResult = _reflection.GeneratedProtocolMessageType('GenerateKeywordIdeaResult', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYWORDIDEARESULT,
  '__module__' : 'google.ads.googleads_v5.proto.services.keyword_plan_idea_service_pb2'
  ,
  '__doc__': """The result of generating keyword ideas.
  
  Attributes:
      text:
          Text of the keyword idea. As in Keyword Plan historical
          metrics, this text may not be an actual keyword, but the
          canonical form of multiple keywords. See
          KeywordPlanKeywordHistoricalMetrics message in
          KeywordPlanService.
      keyword_idea_metrics:
          The historical metrics for the keyword
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.GenerateKeywordIdeaResult)
  })
_sym_db.RegisterMessage(GenerateKeywordIdeaResult)


DESCRIPTOR._options = None
_GENERATEKEYWORDIDEASREQUEST.fields_by_name['language']._options = None

_KEYWORDPLANIDEASERVICE = _descriptor.ServiceDescriptor(
  name='KeywordPlanIdeaService',
  full_name='google.ads.googleads.v5.services.KeywordPlanIdeaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=1596,
  serialized_end=1863,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenerateKeywordIdeas',
    full_name='google.ads.googleads.v5.services.KeywordPlanIdeaService.GenerateKeywordIdeas',
    index=0,
    containing_service=None,
    input_type=_GENERATEKEYWORDIDEASREQUEST,
    output_type=_GENERATEKEYWORDIDEARESPONSE,
    serialized_options=b'\202\323\344\223\0027\"2/v5/customers/{customer_id=*}:generateKeywordIdeas:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYWORDPLANIDEASERVICE)

DESCRIPTOR.services_by_name['KeywordPlanIdeaService'] = _KEYWORDPLANIDEASERVICE

# @@protoc_insertion_point(module_scope)
