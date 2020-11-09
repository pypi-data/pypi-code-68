# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/campaign_experiment_traffic_split_type.proto

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
  name='google/ads/googleads_v3/proto/enums/campaign_experiment_traffic_split_type.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\'CampaignExperimentTrafficSplitTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\nPgoogle/ads/googleads_v3/proto/enums/campaign_experiment_traffic_split_type.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"\x8a\x01\n&CampaignExperimentTrafficSplitTypeEnum\"`\n\"CampaignExperimentTrafficSplitType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x10\n\x0cRANDOM_QUERY\x10\x02\x12\n\n\x06\x43OOKIE\x10\x03\x42\xfc\x01\n!com.google.ads.googleads.v3.enumsB\'CampaignExperimentTrafficSplitTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CAMPAIGNEXPERIMENTTRAFFICSPLITTYPEENUM_CAMPAIGNEXPERIMENTTRAFFICSPLITTYPE = _descriptor.EnumDescriptor(
  name='CampaignExperimentTrafficSplitType',
  full_name='google.ads.googleads.v3.enums.CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitType',
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
      name='RANDOM_QUERY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COOKIE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=188,
  serialized_end=284,
)
_sym_db.RegisterEnumDescriptor(_CAMPAIGNEXPERIMENTTRAFFICSPLITTYPEENUM_CAMPAIGNEXPERIMENTTRAFFICSPLITTYPE)


_CAMPAIGNEXPERIMENTTRAFFICSPLITTYPEENUM = _descriptor.Descriptor(
  name='CampaignExperimentTrafficSplitTypeEnum',
  full_name='google.ads.googleads.v3.enums.CampaignExperimentTrafficSplitTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMPAIGNEXPERIMENTTRAFFICSPLITTYPEENUM_CAMPAIGNEXPERIMENTTRAFFICSPLITTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=284,
)

_CAMPAIGNEXPERIMENTTRAFFICSPLITTYPEENUM_CAMPAIGNEXPERIMENTTRAFFICSPLITTYPE.containing_type = _CAMPAIGNEXPERIMENTTRAFFICSPLITTYPEENUM
DESCRIPTOR.message_types_by_name['CampaignExperimentTrafficSplitTypeEnum'] = _CAMPAIGNEXPERIMENTTRAFFICSPLITTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignExperimentTrafficSplitTypeEnum = _reflection.GeneratedProtocolMessageType('CampaignExperimentTrafficSplitTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNEXPERIMENTTRAFFICSPLITTYPEENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.campaign_experiment_traffic_split_type_pb2'
  ,
  __doc__ = """Container for enum describing campaign experiment traffic split type.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.CampaignExperimentTrafficSplitTypeEnum)
  ))
_sym_db.RegisterMessage(CampaignExperimentTrafficSplitTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
