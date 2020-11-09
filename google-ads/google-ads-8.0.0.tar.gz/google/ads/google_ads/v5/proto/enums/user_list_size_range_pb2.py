# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/enums/user_list_size_range.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/enums/user_list_size_range.proto',
  package='google.ads.googleads.v5.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v5.enumsB\026UserListSizeRangeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V5.Enums\312\002\035Google\\Ads\\GoogleAds\\V5\\Enums\352\002!Google::Ads::GoogleAds::V5::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>google/ads/googleads_v5/proto/enums/user_list_size_range.proto\x12\x1dgoogle.ads.googleads.v5.enums\x1a\x1cgoogle/api/annotations.proto\"\x94\x05\n\x15UserListSizeRangeEnum\"\xfa\x04\n\x11UserListSizeRange\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1a\n\x16LESS_THAN_FIVE_HUNDRED\x10\x02\x12\x1a\n\x16LESS_THAN_ONE_THOUSAND\x10\x03\x12 \n\x1cONE_THOUSAND_TO_TEN_THOUSAND\x10\x04\x12\"\n\x1eTEN_THOUSAND_TO_FIFTY_THOUSAND\x10\x05\x12*\n&FIFTY_THOUSAND_TO_ONE_HUNDRED_THOUSAND\x10\x06\x12\x32\n.ONE_HUNDRED_THOUSAND_TO_THREE_HUNDRED_THOUSAND\x10\x07\x12\x33\n/THREE_HUNDRED_THOUSAND_TO_FIVE_HUNDRED_THOUSAND\x10\x08\x12(\n$FIVE_HUNDRED_THOUSAND_TO_ONE_MILLION\x10\t\x12\x1e\n\x1aONE_MILLION_TO_TWO_MILLION\x10\n\x12 \n\x1cTWO_MILLION_TO_THREE_MILLION\x10\x0b\x12!\n\x1dTHREE_MILLION_TO_FIVE_MILLION\x10\x0c\x12\x1f\n\x1b\x46IVE_MILLION_TO_TEN_MILLION\x10\r\x12!\n\x1dTEN_MILLION_TO_TWENTY_MILLION\x10\x0e\x12$\n TWENTY_MILLION_TO_THIRTY_MILLION\x10\x0f\x12#\n\x1fTHIRTY_MILLION_TO_FIFTY_MILLION\x10\x10\x12\x16\n\x12OVER_FIFTY_MILLION\x10\x11\x42\xeb\x01\n!com.google.ads.googleads.v5.enumsB\x16UserListSizeRangeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V5.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V5\\Enums\xea\x02!Google::Ads::GoogleAds::V5::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_USERLISTSIZERANGEENUM_USERLISTSIZERANGE = _descriptor.EnumDescriptor(
  name='UserListSizeRange',
  full_name='google.ads.googleads.v5.enums.UserListSizeRangeEnum.UserListSizeRange',
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
      name='LESS_THAN_FIVE_HUNDRED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LESS_THAN_ONE_THOUSAND', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONE_THOUSAND_TO_TEN_THOUSAND', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEN_THOUSAND_TO_FIFTY_THOUSAND', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIFTY_THOUSAND_TO_ONE_HUNDRED_THOUSAND', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONE_HUNDRED_THOUSAND_TO_THREE_HUNDRED_THOUSAND', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THREE_HUNDRED_THOUSAND_TO_FIVE_HUNDRED_THOUSAND', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIVE_HUNDRED_THOUSAND_TO_ONE_MILLION', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONE_MILLION_TO_TWO_MILLION', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TWO_MILLION_TO_THREE_MILLION', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THREE_MILLION_TO_FIVE_MILLION', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIVE_MILLION_TO_TEN_MILLION', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEN_MILLION_TO_TWENTY_MILLION', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TWENTY_MILLION_TO_THIRTY_MILLION', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THIRTY_MILLION_TO_FIFTY_MILLION', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OVER_FIFTY_MILLION', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=788,
)
_sym_db.RegisterEnumDescriptor(_USERLISTSIZERANGEENUM_USERLISTSIZERANGE)


_USERLISTSIZERANGEENUM = _descriptor.Descriptor(
  name='UserListSizeRangeEnum',
  full_name='google.ads.googleads.v5.enums.UserListSizeRangeEnum',
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
    _USERLISTSIZERANGEENUM_USERLISTSIZERANGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=788,
)

_USERLISTSIZERANGEENUM_USERLISTSIZERANGE.containing_type = _USERLISTSIZERANGEENUM
DESCRIPTOR.message_types_by_name['UserListSizeRangeEnum'] = _USERLISTSIZERANGEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserListSizeRangeEnum = _reflection.GeneratedProtocolMessageType('UserListSizeRangeEnum', (_message.Message,), {
  'DESCRIPTOR' : _USERLISTSIZERANGEENUM,
  '__module__' : 'google.ads.googleads_v5.proto.enums.user_list_size_range_pb2'
  ,
  '__doc__': """Size range in terms of number of users of a UserList.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.enums.UserListSizeRangeEnum)
  })
_sym_db.RegisterMessage(UserListSizeRangeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
