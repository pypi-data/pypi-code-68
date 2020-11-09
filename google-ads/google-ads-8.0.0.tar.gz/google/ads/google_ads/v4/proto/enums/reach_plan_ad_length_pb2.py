# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/enums/reach_plan_ad_length.proto

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
  name='google/ads/googleads_v4/proto/enums/reach_plan_ad_length.proto',
  package='google.ads.googleads.v4.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v4.enumsB\026ReachPlanAdLengthProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V4.Enums\312\002\035Google\\Ads\\GoogleAds\\V4\\Enums\352\002!Google::Ads::GoogleAds::V4::Enums'),
  serialized_pb=_b('\n>google/ads/googleads_v4/proto/enums/reach_plan_ad_length.proto\x12\x1dgoogle.ads.googleads.v4.enums\x1a\x1cgoogle/api/annotations.proto\"\x96\x01\n\x15ReachPlanAdLengthEnum\"}\n\x11ReachPlanAdLength\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0f\n\x0bSIX_SECONDS\x10\x02\x12\x1d\n\x19\x46IFTEEN_OR_TWENTY_SECONDS\x10\x03\x12\x1a\n\x16TWENTY_SECONDS_OR_MORE\x10\x04\x42\xeb\x01\n!com.google.ads.googleads.v4.enumsB\x16ReachPlanAdLengthProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V4.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V4\\Enums\xea\x02!Google::Ads::GoogleAds::V4::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_REACHPLANADLENGTHENUM_REACHPLANADLENGTH = _descriptor.EnumDescriptor(
  name='ReachPlanAdLength',
  full_name='google.ads.googleads.v4.enums.ReachPlanAdLengthEnum.ReachPlanAdLength',
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
      name='SIX_SECONDS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIFTEEN_OR_TWENTY_SECONDS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWENTY_SECONDS_OR_MORE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=278,
)
_sym_db.RegisterEnumDescriptor(_REACHPLANADLENGTHENUM_REACHPLANADLENGTH)


_REACHPLANADLENGTHENUM = _descriptor.Descriptor(
  name='ReachPlanAdLengthEnum',
  full_name='google.ads.googleads.v4.enums.ReachPlanAdLengthEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REACHPLANADLENGTHENUM_REACHPLANADLENGTH,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=278,
)

_REACHPLANADLENGTHENUM_REACHPLANADLENGTH.containing_type = _REACHPLANADLENGTHENUM
DESCRIPTOR.message_types_by_name['ReachPlanAdLengthEnum'] = _REACHPLANADLENGTHENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReachPlanAdLengthEnum = _reflection.GeneratedProtocolMessageType('ReachPlanAdLengthEnum', (_message.Message,), dict(
  DESCRIPTOR = _REACHPLANADLENGTHENUM,
  __module__ = 'google.ads.googleads_v4.proto.enums.reach_plan_ad_length_pb2'
  ,
  __doc__ = """Message describing length of a plannable video ad.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.enums.ReachPlanAdLengthEnum)
  ))
_sym_db.RegisterMessage(ReachPlanAdLengthEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
