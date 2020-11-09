# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/enums/job_placeholder_field.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/enums/job_placeholder_field.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\031JobsPlaceholderFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?google/ads/googleads_v6/proto/enums/job_placeholder_field.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\xf1\x02\n\x17JobPlaceholderFieldEnum\"\xd5\x02\n\x13JobPlaceholderField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06JOB_ID\x10\x02\x12\x0f\n\x0bLOCATION_ID\x10\x03\x12\t\n\x05TITLE\x10\x04\x12\x0c\n\x08SUBTITLE\x10\x05\x12\x0f\n\x0b\x44\x45SCRIPTION\x10\x06\x12\r\n\tIMAGE_URL\x10\x07\x12\x0c\n\x08\x43\x41TEGORY\x10\x08\x12\x17\n\x13\x43ONTEXTUAL_KEYWORDS\x10\t\x12\x0b\n\x07\x41\x44\x44RESS\x10\n\x12\n\n\x06SALARY\x10\x0b\x12\x0e\n\nFINAL_URLS\x10\x0c\x12\x15\n\x11\x46INAL_MOBILE_URLS\x10\x0e\x12\x10\n\x0cTRACKING_URL\x10\x0f\x12\x14\n\x10\x41NDROID_APP_LINK\x10\x10\x12\x13\n\x0fSIMILAR_JOB_IDS\x10\x11\x12\x10\n\x0cIOS_APP_LINK\x10\x12\x12\x14\n\x10IOS_APP_STORE_ID\x10\x13\x42\xee\x01\n!com.google.ads.googleads.v6.enumsB\x19JobsPlaceholderFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_JOBPLACEHOLDERFIELDENUM_JOBPLACEHOLDERFIELD = _descriptor.EnumDescriptor(
  name='JobPlaceholderField',
  full_name='google.ads.googleads.v6.enums.JobPlaceholderFieldEnum.JobPlaceholderField',
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
      name='JOB_ID', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_ID', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TITLE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUBTITLE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_URL', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONTEXTUAL_KEYWORDS', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SALARY', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URLS', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL_MOBILE_URLS', index=13, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRACKING_URL', index=14, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANDROID_APP_LINK', index=15, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIMILAR_JOB_IDS', index=16, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IOS_APP_LINK', index=17, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IOS_APP_STORE_ID', index=18, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=157,
  serialized_end=498,
)
_sym_db.RegisterEnumDescriptor(_JOBPLACEHOLDERFIELDENUM_JOBPLACEHOLDERFIELD)


_JOBPLACEHOLDERFIELDENUM = _descriptor.Descriptor(
  name='JobPlaceholderFieldEnum',
  full_name='google.ads.googleads.v6.enums.JobPlaceholderFieldEnum',
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
    _JOBPLACEHOLDERFIELDENUM_JOBPLACEHOLDERFIELD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=498,
)

_JOBPLACEHOLDERFIELDENUM_JOBPLACEHOLDERFIELD.containing_type = _JOBPLACEHOLDERFIELDENUM
DESCRIPTOR.message_types_by_name['JobPlaceholderFieldEnum'] = _JOBPLACEHOLDERFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobPlaceholderFieldEnum = _reflection.GeneratedProtocolMessageType('JobPlaceholderFieldEnum', (_message.Message,), {
  'DESCRIPTOR' : _JOBPLACEHOLDERFIELDENUM,
  '__module__' : 'google.ads.googleads_v6.proto.enums.job_placeholder_field_pb2'
  ,
  '__doc__': """Values for Job placeholder fields. For more information about dynamic
  remarketing feeds, see https://support.google.com/google-
  ads/answer/6053288.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.JobPlaceholderFieldEnum)
  })
_sym_db.RegisterMessage(JobPlaceholderFieldEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
