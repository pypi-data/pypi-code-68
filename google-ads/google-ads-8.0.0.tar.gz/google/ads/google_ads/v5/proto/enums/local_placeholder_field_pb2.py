# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/enums/local_placeholder_field.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/enums/local_placeholder_field.proto',
  package='google.ads.googleads.v5.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v5.enumsB\032LocalPlaceholderFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V5.Enums\312\002\035Google\\Ads\\GoogleAds\\V5\\Enums\352\002!Google::Ads::GoogleAds::V5::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nAgoogle/ads/googleads_v5/proto/enums/local_placeholder_field.proto\x12\x1dgoogle.ads.googleads.v5.enums\x1a\x1cgoogle/api/annotations.proto\"\xa8\x03\n\x19LocalPlaceholderFieldEnum\"\x8a\x03\n\x15LocalPlaceholderField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07\x44\x45\x41L_ID\x10\x02\x12\r\n\tDEAL_NAME\x10\x03\x12\x0c\n\x08SUBTITLE\x10\x04\x12\x0f\n\x0b\x44\x45SCRIPTION\x10\x05\x12\t\n\x05PRICE\x10\x06\x12\x13\n\x0f\x46ORMATTED_PRICE\x10\x07\x12\x0e\n\nSALE_PRICE\x10\x08\x12\x18\n\x14\x46ORMATTED_SALE_PRICE\x10\t\x12\r\n\tIMAGE_URL\x10\n\x12\x0b\n\x07\x41\x44\x44RESS\x10\x0b\x12\x0c\n\x08\x43\x41TEGORY\x10\x0c\x12\x17\n\x13\x43ONTEXTUAL_KEYWORDS\x10\r\x12\x0e\n\nFINAL_URLS\x10\x0e\x12\x15\n\x11\x46INAL_MOBILE_URLS\x10\x0f\x12\x10\n\x0cTRACKING_URL\x10\x10\x12\x14\n\x10\x41NDROID_APP_LINK\x10\x11\x12\x14\n\x10SIMILAR_DEAL_IDS\x10\x12\x12\x10\n\x0cIOS_APP_LINK\x10\x13\x12\x14\n\x10IOS_APP_STORE_ID\x10\x14\x42\xef\x01\n!com.google.ads.googleads.v5.enumsB\x1aLocalPlaceholderFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V5.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V5\\Enums\xea\x02!Google::Ads::GoogleAds::V5::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_LOCALPLACEHOLDERFIELDENUM_LOCALPLACEHOLDERFIELD = _descriptor.EnumDescriptor(
  name='LocalPlaceholderField',
  full_name='google.ads.googleads.v5.enums.LocalPlaceholderFieldEnum.LocalPlaceholderField',
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
      name='DEAL_ID', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEAL_NAME', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUBTITLE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRICE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORMATTED_PRICE', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SALE_PRICE', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORMATTED_SALE_PRICE', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_URL', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONTEXTUAL_KEYWORDS', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URLS', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL_MOBILE_URLS', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRACKING_URL', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANDROID_APP_LINK', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIMILAR_DEAL_IDS', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IOS_APP_LINK', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IOS_APP_STORE_ID', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=161,
  serialized_end=555,
)
_sym_db.RegisterEnumDescriptor(_LOCALPLACEHOLDERFIELDENUM_LOCALPLACEHOLDERFIELD)


_LOCALPLACEHOLDERFIELDENUM = _descriptor.Descriptor(
  name='LocalPlaceholderFieldEnum',
  full_name='google.ads.googleads.v5.enums.LocalPlaceholderFieldEnum',
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
    _LOCALPLACEHOLDERFIELDENUM_LOCALPLACEHOLDERFIELD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=555,
)

_LOCALPLACEHOLDERFIELDENUM_LOCALPLACEHOLDERFIELD.containing_type = _LOCALPLACEHOLDERFIELDENUM
DESCRIPTOR.message_types_by_name['LocalPlaceholderFieldEnum'] = _LOCALPLACEHOLDERFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocalPlaceholderFieldEnum = _reflection.GeneratedProtocolMessageType('LocalPlaceholderFieldEnum', (_message.Message,), {
  'DESCRIPTOR' : _LOCALPLACEHOLDERFIELDENUM,
  '__module__' : 'google.ads.googleads_v5.proto.enums.local_placeholder_field_pb2'
  ,
  '__doc__': """Values for Local placeholder fields. For more information about
  dynamic remarketing feeds, see https://support.google.com/google-
  ads/answer/6053288.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.enums.LocalPlaceholderFieldEnum)
  })
_sym_db.RegisterMessage(LocalPlaceholderFieldEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
