# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/errors/feed_mapping_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/errors/feed_mapping_error.proto',
  package='google.ads.googleads.v5.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v5.errorsB\025FeedMappingErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V5.Errors\312\002\036Google\\Ads\\GoogleAds\\V5\\Errors\352\002\"Google::Ads::GoogleAds::V5::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=google/ads/googleads_v5/proto/errors/feed_mapping_error.proto\x12\x1egoogle.ads.googleads.v5.errors\x1a\x1cgoogle/api/annotations.proto\"\x92\x06\n\x14\x46\x65\x65\x64MappingErrorEnum\"\xf9\x05\n\x10\x46\x65\x65\x64MappingError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1d\n\x19INVALID_PLACEHOLDER_FIELD\x10\x02\x12\x1b\n\x17INVALID_CRITERION_FIELD\x10\x03\x12\x1c\n\x18INVALID_PLACEHOLDER_TYPE\x10\x04\x12\x1a\n\x16INVALID_CRITERION_TYPE\x10\x05\x12\x1f\n\x1bNO_ATTRIBUTE_FIELD_MAPPINGS\x10\x07\x12 \n\x1c\x46\x45\x45\x44_ATTRIBUTE_TYPE_MISMATCH\x10\x08\x12\x38\n4CANNOT_OPERATE_ON_MAPPINGS_FOR_SYSTEM_GENERATED_FEED\x10\t\x12*\n&MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_TYPE\x10\n\x12(\n$MULTIPLE_MAPPINGS_FOR_CRITERION_TYPE\x10\x0b\x12+\n\'MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_FIELD\x10\x0c\x12)\n%MULTIPLE_MAPPINGS_FOR_CRITERION_FIELD\x10\r\x12\'\n#UNEXPECTED_ATTRIBUTE_FIELD_MAPPINGS\x10\x0e\x12.\n*LOCATION_PLACEHOLDER_ONLY_FOR_PLACES_FEEDS\x10\x0f\x12)\n%CANNOT_MODIFY_MAPPINGS_FOR_TYPED_FEED\x10\x10\x12:\n6INVALID_PLACEHOLDER_TYPE_FOR_NON_SYSTEM_GENERATED_FEED\x10\x11\x12;\n7INVALID_PLACEHOLDER_TYPE_FOR_SYSTEM_GENERATED_FEED_TYPE\x10\x12\x12)\n%ATTRIBUTE_FIELD_MAPPING_MISSING_FIELD\x10\x13\x42\xf0\x01\n\"com.google.ads.googleads.v5.errorsB\x15\x46\x65\x65\x64MappingErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V5.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V5\\Errors\xea\x02\"Google::Ads::GoogleAds::V5::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDMAPPINGERRORENUM_FEEDMAPPINGERROR = _descriptor.EnumDescriptor(
  name='FeedMappingError',
  full_name='google.ads.googleads.v5.errors.FeedMappingErrorEnum.FeedMappingError',
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
      name='INVALID_PLACEHOLDER_FIELD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CRITERION_FIELD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PLACEHOLDER_TYPE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CRITERION_TYPE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_ATTRIBUTE_FIELD_MAPPINGS', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FEED_ATTRIBUTE_TYPE_MISMATCH', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_OPERATE_ON_MAPPINGS_FOR_SYSTEM_GENERATED_FEED', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_TYPE', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_MAPPINGS_FOR_CRITERION_TYPE', index=10, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_FIELD', index=11, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_MAPPINGS_FOR_CRITERION_FIELD', index=12, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNEXPECTED_ATTRIBUTE_FIELD_MAPPINGS', index=13, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_PLACEHOLDER_ONLY_FOR_PLACES_FEEDS', index=14, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_MODIFY_MAPPINGS_FOR_TYPED_FEED', index=15, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PLACEHOLDER_TYPE_FOR_NON_SYSTEM_GENERATED_FEED', index=16, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PLACEHOLDER_TYPE_FOR_SYSTEM_GENERATED_FEED_TYPE', index=17, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ATTRIBUTE_FIELD_MAPPING_MISSING_FIELD', index=18, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=914,
)
_sym_db.RegisterEnumDescriptor(_FEEDMAPPINGERRORENUM_FEEDMAPPINGERROR)


_FEEDMAPPINGERRORENUM = _descriptor.Descriptor(
  name='FeedMappingErrorEnum',
  full_name='google.ads.googleads.v5.errors.FeedMappingErrorEnum',
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
    _FEEDMAPPINGERRORENUM_FEEDMAPPINGERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=914,
)

_FEEDMAPPINGERRORENUM_FEEDMAPPINGERROR.containing_type = _FEEDMAPPINGERRORENUM
DESCRIPTOR.message_types_by_name['FeedMappingErrorEnum'] = _FEEDMAPPINGERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedMappingErrorEnum = _reflection.GeneratedProtocolMessageType('FeedMappingErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _FEEDMAPPINGERRORENUM,
  '__module__' : 'google.ads.googleads_v5.proto.errors.feed_mapping_error_pb2'
  ,
  '__doc__': """Container for enum describing possible feed item errors.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.errors.FeedMappingErrorEnum)
  })
_sym_db.RegisterMessage(FeedMappingErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
