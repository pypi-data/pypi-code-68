# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/enums/user_list_combined_rule_operator.proto

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
  name='google/ads/googleads_v4/proto/enums/user_list_combined_rule_operator.proto',
  package='google.ads.googleads.v4.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v4.enumsB!UserListCombinedRuleOperatorProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V4.Enums\312\002\035Google\\Ads\\GoogleAds\\V4\\Enums\352\002!Google::Ads::GoogleAds::V4::Enums'),
  serialized_pb=_b('\nJgoogle/ads/googleads_v4/proto/enums/user_list_combined_rule_operator.proto\x12\x1dgoogle.ads.googleads.v4.enums\x1a\x1cgoogle/api/annotations.proto\"v\n UserListCombinedRuleOperatorEnum\"R\n\x1cUserListCombinedRuleOperator\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03\x41ND\x10\x02\x12\x0b\n\x07\x41ND_NOT\x10\x03\x42\xf6\x01\n!com.google.ads.googleads.v4.enumsB!UserListCombinedRuleOperatorProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V4.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V4\\Enums\xea\x02!Google::Ads::GoogleAds::V4::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_USERLISTCOMBINEDRULEOPERATORENUM_USERLISTCOMBINEDRULEOPERATOR = _descriptor.EnumDescriptor(
  name='UserListCombinedRuleOperator',
  full_name='google.ads.googleads.v4.enums.UserListCombinedRuleOperatorEnum.UserListCombinedRuleOperator',
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
      name='AND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AND_NOT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=175,
  serialized_end=257,
)
_sym_db.RegisterEnumDescriptor(_USERLISTCOMBINEDRULEOPERATORENUM_USERLISTCOMBINEDRULEOPERATOR)


_USERLISTCOMBINEDRULEOPERATORENUM = _descriptor.Descriptor(
  name='UserListCombinedRuleOperatorEnum',
  full_name='google.ads.googleads.v4.enums.UserListCombinedRuleOperatorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERLISTCOMBINEDRULEOPERATORENUM_USERLISTCOMBINEDRULEOPERATOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=257,
)

_USERLISTCOMBINEDRULEOPERATORENUM_USERLISTCOMBINEDRULEOPERATOR.containing_type = _USERLISTCOMBINEDRULEOPERATORENUM
DESCRIPTOR.message_types_by_name['UserListCombinedRuleOperatorEnum'] = _USERLISTCOMBINEDRULEOPERATORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserListCombinedRuleOperatorEnum = _reflection.GeneratedProtocolMessageType('UserListCombinedRuleOperatorEnum', (_message.Message,), dict(
  DESCRIPTOR = _USERLISTCOMBINEDRULEOPERATORENUM,
  __module__ = 'google.ads.googleads_v4.proto.enums.user_list_combined_rule_operator_pb2'
  ,
  __doc__ = """Logical operator connecting two rules.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.enums.UserListCombinedRuleOperatorEnum)
  ))
_sym_db.RegisterMessage(UserListCombinedRuleOperatorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
