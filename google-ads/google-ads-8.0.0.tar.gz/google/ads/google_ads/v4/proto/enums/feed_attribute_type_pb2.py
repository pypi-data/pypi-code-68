# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/enums/feed_attribute_type.proto

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
  name='google/ads/googleads_v4/proto/enums/feed_attribute_type.proto',
  package='google.ads.googleads.v4.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v4.enumsB\026FeedAttributeTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V4.Enums\312\002\035Google\\Ads\\GoogleAds\\V4\\Enums\352\002!Google::Ads::GoogleAds::V4::Enums'),
  serialized_pb=_b('\n=google/ads/googleads_v4/proto/enums/feed_attribute_type.proto\x12\x1dgoogle.ads.googleads.v4.enums\x1a\x1cgoogle/api/annotations.proto\"\x84\x02\n\x15\x46\x65\x65\x64\x41ttributeTypeEnum\"\xea\x01\n\x11\x46\x65\x65\x64\x41ttributeType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\t\n\x05INT64\x10\x02\x12\n\n\x06\x44OUBLE\x10\x03\x12\n\n\x06STRING\x10\x04\x12\x0b\n\x07\x42OOLEAN\x10\x05\x12\x07\n\x03URL\x10\x06\x12\r\n\tDATE_TIME\x10\x07\x12\x0e\n\nINT64_LIST\x10\x08\x12\x0f\n\x0b\x44OUBLE_LIST\x10\t\x12\x0f\n\x0bSTRING_LIST\x10\n\x12\x10\n\x0c\x42OOLEAN_LIST\x10\x0b\x12\x0c\n\x08URL_LIST\x10\x0c\x12\x12\n\x0e\x44\x41TE_TIME_LIST\x10\r\x12\t\n\x05PRICE\x10\x0e\x42\xeb\x01\n!com.google.ads.googleads.v4.enumsB\x16\x46\x65\x65\x64\x41ttributeTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V4.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V4\\Enums\xea\x02!Google::Ads::GoogleAds::V4::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDATTRIBUTETYPEENUM_FEEDATTRIBUTETYPE = _descriptor.EnumDescriptor(
  name='FeedAttributeType',
  full_name='google.ads.googleads.v4.enums.FeedAttributeTypeEnum.FeedAttributeType',
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
      name='INT64', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_TIME', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64_LIST', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_LIST', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING_LIST', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN_LIST', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_LIST', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_TIME_LIST', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE', index=14, number=14,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=387,
)
_sym_db.RegisterEnumDescriptor(_FEEDATTRIBUTETYPEENUM_FEEDATTRIBUTETYPE)


_FEEDATTRIBUTETYPEENUM = _descriptor.Descriptor(
  name='FeedAttributeTypeEnum',
  full_name='google.ads.googleads.v4.enums.FeedAttributeTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDATTRIBUTETYPEENUM_FEEDATTRIBUTETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=387,
)

_FEEDATTRIBUTETYPEENUM_FEEDATTRIBUTETYPE.containing_type = _FEEDATTRIBUTETYPEENUM
DESCRIPTOR.message_types_by_name['FeedAttributeTypeEnum'] = _FEEDATTRIBUTETYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedAttributeTypeEnum = _reflection.GeneratedProtocolMessageType('FeedAttributeTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDATTRIBUTETYPEENUM,
  __module__ = 'google.ads.googleads_v4.proto.enums.feed_attribute_type_pb2'
  ,
  __doc__ = """Container for enum describing possible data types for a feed attribute.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.enums.FeedAttributeTypeEnum)
  ))
_sym_db.RegisterMessage(FeedAttributeTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
