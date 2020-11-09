# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/errors/custom_interest_error.proto

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
  name='google/ads/googleads_v4/proto/errors/custom_interest_error.proto',
  package='google.ads.googleads.v4.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v4.errorsB\030CustomInterestErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v4/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V4.Errors\312\002\036Google\\Ads\\GoogleAds\\V4\\Errors\352\002\"Google::Ads::GoogleAds::V4::Errors'),
  serialized_pb=_b('\n@google/ads/googleads_v4/proto/errors/custom_interest_error.proto\x12\x1egoogle.ads.googleads.v4.errors\x1a\x1cgoogle/api/annotations.proto\"\xd9\x02\n\x17\x43ustomInterestErrorEnum\"\xbd\x02\n\x13\x43ustomInterestError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11NAME_ALREADY_USED\x10\x02\x12\x46\nBCUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE\x10\x03\x12 \n\x1cTYPE_AND_PARAMETER_NOT_FOUND\x10\x04\x12&\n\"TYPE_AND_PARAMETER_ALREADY_EXISTED\x10\x05\x12\'\n#INVALID_CUSTOM_INTEREST_MEMBER_TYPE\x10\x06\x12\x1e\n\x1a\x43\x41NNOT_REMOVE_WHILE_IN_USE\x10\x07\x12\x16\n\x12\x43\x41NNOT_CHANGE_TYPE\x10\x08\x42\xf3\x01\n\"com.google.ads.googleads.v4.errorsB\x18\x43ustomInterestErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v4/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V4.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V4\\Errors\xea\x02\"Google::Ads::GoogleAds::V4::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CUSTOMINTERESTERRORENUM_CUSTOMINTERESTERROR = _descriptor.EnumDescriptor(
  name='CustomInterestError',
  full_name='google.ads.googleads.v4.errors.CustomInterestErrorEnum.CustomInterestError',
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
      name='NAME_ALREADY_USED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_AND_PARAMETER_NOT_FOUND', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_AND_PARAMETER_ALREADY_EXISTED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CUSTOM_INTEREST_MEMBER_TYPE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_REMOVE_WHILE_IN_USE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CHANGE_TYPE', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=159,
  serialized_end=476,
)
_sym_db.RegisterEnumDescriptor(_CUSTOMINTERESTERRORENUM_CUSTOMINTERESTERROR)


_CUSTOMINTERESTERRORENUM = _descriptor.Descriptor(
  name='CustomInterestErrorEnum',
  full_name='google.ads.googleads.v4.errors.CustomInterestErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CUSTOMINTERESTERRORENUM_CUSTOMINTERESTERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=476,
)

_CUSTOMINTERESTERRORENUM_CUSTOMINTERESTERROR.containing_type = _CUSTOMINTERESTERRORENUM
DESCRIPTOR.message_types_by_name['CustomInterestErrorEnum'] = _CUSTOMINTERESTERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomInterestErrorEnum = _reflection.GeneratedProtocolMessageType('CustomInterestErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMINTERESTERRORENUM,
  __module__ = 'google.ads.googleads_v4.proto.errors.custom_interest_error_pb2'
  ,
  __doc__ = """Container for enum describing possible custom interest errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.errors.CustomInterestErrorEnum)
  ))
_sym_db.RegisterMessage(CustomInterestErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
