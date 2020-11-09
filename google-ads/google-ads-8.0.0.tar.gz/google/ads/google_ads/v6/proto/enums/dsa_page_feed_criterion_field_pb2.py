# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/enums/dsa_page_feed_criterion_field.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/enums/dsa_page_feed_criterion_field.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\036DsaPageFeedCriterionFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nGgoogle/ads/googleads_v6/proto/enums/dsa_page_feed_criterion_field.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"s\n\x1d\x44saPageFeedCriterionFieldEnum\"R\n\x19\x44saPageFeedCriterionField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08PAGE_URL\x10\x02\x12\t\n\x05LABEL\x10\x03\x42\xf3\x01\n!com.google.ads.googleads.v6.enumsB\x1e\x44saPageFeedCriterionFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_DSAPAGEFEEDCRITERIONFIELDENUM_DSAPAGEFEEDCRITERIONFIELD = _descriptor.EnumDescriptor(
  name='DsaPageFeedCriterionField',
  full_name='google.ads.googleads.v6.enums.DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField',
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
      name='PAGE_URL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LABEL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=169,
  serialized_end=251,
)
_sym_db.RegisterEnumDescriptor(_DSAPAGEFEEDCRITERIONFIELDENUM_DSAPAGEFEEDCRITERIONFIELD)


_DSAPAGEFEEDCRITERIONFIELDENUM = _descriptor.Descriptor(
  name='DsaPageFeedCriterionFieldEnum',
  full_name='google.ads.googleads.v6.enums.DsaPageFeedCriterionFieldEnum',
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
    _DSAPAGEFEEDCRITERIONFIELDENUM_DSAPAGEFEEDCRITERIONFIELD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=251,
)

_DSAPAGEFEEDCRITERIONFIELDENUM_DSAPAGEFEEDCRITERIONFIELD.containing_type = _DSAPAGEFEEDCRITERIONFIELDENUM
DESCRIPTOR.message_types_by_name['DsaPageFeedCriterionFieldEnum'] = _DSAPAGEFEEDCRITERIONFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DsaPageFeedCriterionFieldEnum = _reflection.GeneratedProtocolMessageType('DsaPageFeedCriterionFieldEnum', (_message.Message,), {
  'DESCRIPTOR' : _DSAPAGEFEEDCRITERIONFIELDENUM,
  '__module__' : 'google.ads.googleads_v6.proto.enums.dsa_page_feed_criterion_field_pb2'
  ,
  '__doc__': """Values for Dynamic Search Ad Page Feed criterion fields.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.DsaPageFeedCriterionFieldEnum)
  })
_sym_db.RegisterMessage(DsaPageFeedCriterionFieldEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
