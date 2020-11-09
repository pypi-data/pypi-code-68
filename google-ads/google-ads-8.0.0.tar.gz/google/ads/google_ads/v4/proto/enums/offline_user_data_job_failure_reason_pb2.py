# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/enums/offline_user_data_job_failure_reason.proto

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
  name='google/ads/googleads_v4/proto/enums/offline_user_data_job_failure_reason.proto',
  package='google.ads.googleads.v4.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v4.enumsB$OfflineUserDataJobFailureReasonProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V4.Enums\312\002\035Google\\Ads\\GoogleAds\\V4\\Enums\352\002!Google::Ads::GoogleAds::V4::Enums'),
  serialized_pb=_b('\nNgoogle/ads/googleads_v4/proto/enums/offline_user_data_job_failure_reason.proto\x12\x1dgoogle.ads.googleads.v4.enums\x1a\x1cgoogle/api/annotations.proto\"\xad\x01\n#OfflineUserDataJobFailureReasonEnum\"\x85\x01\n\x1fOfflineUserDataJobFailureReason\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12%\n!INSUFFICIENT_MATCHED_TRANSACTIONS\x10\x02\x12\x1d\n\x19INSUFFICIENT_TRANSACTIONS\x10\x03\x42\xf9\x01\n!com.google.ads.googleads.v4.enumsB$OfflineUserDataJobFailureReasonProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V4.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V4\\Enums\xea\x02!Google::Ads::GoogleAds::V4::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_OFFLINEUSERDATAJOBFAILUREREASONENUM_OFFLINEUSERDATAJOBFAILUREREASON = _descriptor.EnumDescriptor(
  name='OfflineUserDataJobFailureReason',
  full_name='google.ads.googleads.v4.enums.OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason',
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
      name='INSUFFICIENT_MATCHED_TRANSACTIONS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSUFFICIENT_TRANSACTIONS', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=184,
  serialized_end=317,
)
_sym_db.RegisterEnumDescriptor(_OFFLINEUSERDATAJOBFAILUREREASONENUM_OFFLINEUSERDATAJOBFAILUREREASON)


_OFFLINEUSERDATAJOBFAILUREREASONENUM = _descriptor.Descriptor(
  name='OfflineUserDataJobFailureReasonEnum',
  full_name='google.ads.googleads.v4.enums.OfflineUserDataJobFailureReasonEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OFFLINEUSERDATAJOBFAILUREREASONENUM_OFFLINEUSERDATAJOBFAILUREREASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=317,
)

_OFFLINEUSERDATAJOBFAILUREREASONENUM_OFFLINEUSERDATAJOBFAILUREREASON.containing_type = _OFFLINEUSERDATAJOBFAILUREREASONENUM
DESCRIPTOR.message_types_by_name['OfflineUserDataJobFailureReasonEnum'] = _OFFLINEUSERDATAJOBFAILUREREASONENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OfflineUserDataJobFailureReasonEnum = _reflection.GeneratedProtocolMessageType('OfflineUserDataJobFailureReasonEnum', (_message.Message,), dict(
  DESCRIPTOR = _OFFLINEUSERDATAJOBFAILUREREASONENUM,
  __module__ = 'google.ads.googleads_v4.proto.enums.offline_user_data_job_failure_reason_pb2'
  ,
  __doc__ = """Container for enum describing reasons why an offline user data job
  failed to be processed.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.enums.OfflineUserDataJobFailureReasonEnum)
  ))
_sym_db.RegisterMessage(OfflineUserDataJobFailureReasonEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
