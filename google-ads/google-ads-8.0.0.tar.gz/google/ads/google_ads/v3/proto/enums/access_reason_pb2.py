# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/access_reason.proto

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
  name='google/ads/googleads_v3/proto/enums/access_reason.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\021AccessReasonProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\n7google/ads/googleads_v3/proto/enums/access_reason.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"\x85\x01\n\x10\x41\x63\x63\x65ssReasonEnum\"q\n\x0c\x41\x63\x63\x65ssReason\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\t\n\x05OWNED\x10\x02\x12\n\n\x06SHARED\x10\x03\x12\x0c\n\x08LICENSED\x10\x04\x12\x0e\n\nSUBSCRIBED\x10\x05\x12\x0e\n\nAFFILIATED\x10\x06\x42\xe6\x01\n!com.google.ads.googleads.v3.enumsB\x11\x41\x63\x63\x65ssReasonProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ACCESSREASONENUM_ACCESSREASON = _descriptor.EnumDescriptor(
  name='AccessReason',
  full_name='google.ads.googleads.v3.enums.AccessReasonEnum.AccessReason',
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
      name='OWNED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LICENSED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AFFILIATED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=141,
  serialized_end=254,
)
_sym_db.RegisterEnumDescriptor(_ACCESSREASONENUM_ACCESSREASON)


_ACCESSREASONENUM = _descriptor.Descriptor(
  name='AccessReasonEnum',
  full_name='google.ads.googleads.v3.enums.AccessReasonEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCESSREASONENUM_ACCESSREASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=254,
)

_ACCESSREASONENUM_ACCESSREASON.containing_type = _ACCESSREASONENUM
DESCRIPTOR.message_types_by_name['AccessReasonEnum'] = _ACCESSREASONENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessReasonEnum = _reflection.GeneratedProtocolMessageType('AccessReasonEnum', (_message.Message,), dict(
  DESCRIPTOR = _ACCESSREASONENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.access_reason_pb2'
  ,
  __doc__ = """Indicates the way the resource such as user list is related to a user.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.AccessReasonEnum)
  ))
_sym_db.RegisterMessage(AccessReasonEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
