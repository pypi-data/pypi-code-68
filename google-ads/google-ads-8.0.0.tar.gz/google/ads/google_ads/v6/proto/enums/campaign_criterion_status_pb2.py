# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/enums/campaign_criterion_status.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/enums/campaign_criterion_status.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\034CampaignCriterionStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCgoogle/ads/googleads_v6/proto/enums/campaign_criterion_status.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"|\n\x1b\x43\x61mpaignCriterionStatusEnum\"]\n\x17\x43\x61mpaignCriterionStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07\x45NABLED\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\x0b\n\x07REMOVED\x10\x04\x42\xf1\x01\n!com.google.ads.googleads.v6.enumsB\x1c\x43\x61mpaignCriterionStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CAMPAIGNCRITERIONSTATUSENUM_CAMPAIGNCRITERIONSTATUS = _descriptor.EnumDescriptor(
  name='CampaignCriterionStatus',
  full_name='google.ads.googleads.v6.enums.CampaignCriterionStatusEnum.CampaignCriterionStatus',
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
      name='ENABLED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REMOVED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=163,
  serialized_end=256,
)
_sym_db.RegisterEnumDescriptor(_CAMPAIGNCRITERIONSTATUSENUM_CAMPAIGNCRITERIONSTATUS)


_CAMPAIGNCRITERIONSTATUSENUM = _descriptor.Descriptor(
  name='CampaignCriterionStatusEnum',
  full_name='google.ads.googleads.v6.enums.CampaignCriterionStatusEnum',
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
    _CAMPAIGNCRITERIONSTATUSENUM_CAMPAIGNCRITERIONSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=256,
)

_CAMPAIGNCRITERIONSTATUSENUM_CAMPAIGNCRITERIONSTATUS.containing_type = _CAMPAIGNCRITERIONSTATUSENUM
DESCRIPTOR.message_types_by_name['CampaignCriterionStatusEnum'] = _CAMPAIGNCRITERIONSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignCriterionStatusEnum = _reflection.GeneratedProtocolMessageType('CampaignCriterionStatusEnum', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNCRITERIONSTATUSENUM,
  '__module__' : 'google.ads.googleads_v6.proto.enums.campaign_criterion_status_pb2'
  ,
  '__doc__': """Message describing CampaignCriterion statuses.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.CampaignCriterionStatusEnum)
  })
_sym_db.RegisterMessage(CampaignCriterionStatusEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
