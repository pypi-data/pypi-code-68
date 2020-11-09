# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/enums/user_list_prepopulation_status.proto

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
  name='google/ads/googleads_v4/proto/enums/user_list_prepopulation_status.proto',
  package='google.ads.googleads.v4.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v4.enumsB UserListPrepopulationStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V4.Enums\312\002\035Google\\Ads\\GoogleAds\\V4\\Enums\352\002!Google::Ads::GoogleAds::V4::Enums'),
  serialized_pb=_b('\nHgoogle/ads/googleads_v4/proto/enums/user_list_prepopulation_status.proto\x12\x1dgoogle.ads.googleads.v4.enums\x1a\x1cgoogle/api/annotations.proto\"\x87\x01\n\x1fUserListPrepopulationStatusEnum\"d\n\x1bUserListPrepopulationStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\r\n\tREQUESTED\x10\x02\x12\x0c\n\x08\x46INISHED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x42\xf5\x01\n!com.google.ads.googleads.v4.enumsB UserListPrepopulationStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V4.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V4\\Enums\xea\x02!Google::Ads::GoogleAds::V4::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_USERLISTPREPOPULATIONSTATUSENUM_USERLISTPREPOPULATIONSTATUS = _descriptor.EnumDescriptor(
  name='UserListPrepopulationStatus',
  full_name='google.ads.googleads.v4.enums.UserListPrepopulationStatusEnum.UserListPrepopulationStatus',
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
      name='REQUESTED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISHED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=173,
  serialized_end=273,
)
_sym_db.RegisterEnumDescriptor(_USERLISTPREPOPULATIONSTATUSENUM_USERLISTPREPOPULATIONSTATUS)


_USERLISTPREPOPULATIONSTATUSENUM = _descriptor.Descriptor(
  name='UserListPrepopulationStatusEnum',
  full_name='google.ads.googleads.v4.enums.UserListPrepopulationStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERLISTPREPOPULATIONSTATUSENUM_USERLISTPREPOPULATIONSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=273,
)

_USERLISTPREPOPULATIONSTATUSENUM_USERLISTPREPOPULATIONSTATUS.containing_type = _USERLISTPREPOPULATIONSTATUSENUM
DESCRIPTOR.message_types_by_name['UserListPrepopulationStatusEnum'] = _USERLISTPREPOPULATIONSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserListPrepopulationStatusEnum = _reflection.GeneratedProtocolMessageType('UserListPrepopulationStatusEnum', (_message.Message,), dict(
  DESCRIPTOR = _USERLISTPREPOPULATIONSTATUSENUM,
  __module__ = 'google.ads.googleads_v4.proto.enums.user_list_prepopulation_status_pb2'
  ,
  __doc__ = """Indicates status of prepopulation based on the rule.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.enums.UserListPrepopulationStatusEnum)
  ))
_sym_db.RegisterMessage(UserListPrepopulationStatusEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
