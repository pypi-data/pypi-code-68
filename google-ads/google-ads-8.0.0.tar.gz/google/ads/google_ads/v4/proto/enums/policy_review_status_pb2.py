# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/enums/policy_review_status.proto

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
  name='google/ads/googleads_v4/proto/enums/policy_review_status.proto',
  package='google.ads.googleads.v4.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v4.enumsB\027PolicyReviewStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V4.Enums\312\002\035Google\\Ads\\GoogleAds\\V4\\Enums\352\002!Google::Ads::GoogleAds::V4::Enums'),
  serialized_pb=_b('\n>google/ads/googleads_v4/proto/enums/policy_review_status.proto\x12\x1dgoogle.ads.googleads.v4.enums\x1a\x1cgoogle/api/annotations.proto\"\x9d\x01\n\x16PolicyReviewStatusEnum\"\x82\x01\n\x12PolicyReviewStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12REVIEW_IN_PROGRESS\x10\x02\x12\x0c\n\x08REVIEWED\x10\x03\x12\x10\n\x0cUNDER_APPEAL\x10\x04\x12\x16\n\x12\x45LIGIBLE_MAY_SERVE\x10\x05\x42\xec\x01\n!com.google.ads.googleads.v4.enumsB\x17PolicyReviewStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V4.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V4\\Enums\xea\x02!Google::Ads::GoogleAds::V4::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_POLICYREVIEWSTATUSENUM_POLICYREVIEWSTATUS = _descriptor.EnumDescriptor(
  name='PolicyReviewStatus',
  full_name='google.ads.googleads.v4.enums.PolicyReviewStatusEnum.PolicyReviewStatus',
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
      name='REVIEW_IN_PROGRESS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVIEWED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDER_APPEAL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELIGIBLE_MAY_SERVE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=155,
  serialized_end=285,
)
_sym_db.RegisterEnumDescriptor(_POLICYREVIEWSTATUSENUM_POLICYREVIEWSTATUS)


_POLICYREVIEWSTATUSENUM = _descriptor.Descriptor(
  name='PolicyReviewStatusEnum',
  full_name='google.ads.googleads.v4.enums.PolicyReviewStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POLICYREVIEWSTATUSENUM_POLICYREVIEWSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=285,
)

_POLICYREVIEWSTATUSENUM_POLICYREVIEWSTATUS.containing_type = _POLICYREVIEWSTATUSENUM
DESCRIPTOR.message_types_by_name['PolicyReviewStatusEnum'] = _POLICYREVIEWSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PolicyReviewStatusEnum = _reflection.GeneratedProtocolMessageType('PolicyReviewStatusEnum', (_message.Message,), dict(
  DESCRIPTOR = _POLICYREVIEWSTATUSENUM,
  __module__ = 'google.ads.googleads_v4.proto.enums.policy_review_status_pb2'
  ,
  __doc__ = """Container for enum describing possible policy review statuses.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.enums.PolicyReviewStatusEnum)
  ))
_sym_db.RegisterMessage(PolicyReviewStatusEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
