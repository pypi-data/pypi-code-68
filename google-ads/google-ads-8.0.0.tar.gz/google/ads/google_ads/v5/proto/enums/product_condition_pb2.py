# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/enums/product_condition.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/enums/product_condition.proto',
  package='google.ads.googleads.v5.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v5.enumsB\025ProductConditionProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V5.Enums\312\002\035Google\\Ads\\GoogleAds\\V5\\Enums\352\002!Google::Ads::GoogleAds::V5::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;google/ads/googleads_v5/proto/enums/product_condition.proto\x12\x1dgoogle.ads.googleads.v5.enums\x1a\x1cgoogle/api/annotations.proto\"l\n\x14ProductConditionEnum\"T\n\x10ProductCondition\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03NEW\x10\x03\x12\x0f\n\x0bREFURBISHED\x10\x04\x12\x08\n\x04USED\x10\x05\x42\xea\x01\n!com.google.ads.googleads.v5.enumsB\x15ProductConditionProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V5.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V5\\Enums\xea\x02!Google::Ads::GoogleAds::V5::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PRODUCTCONDITIONENUM_PRODUCTCONDITION = _descriptor.EnumDescriptor(
  name='ProductCondition',
  full_name='google.ads.googleads.v5.enums.ProductConditionEnum.ProductCondition',
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
      name='NEW', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REFURBISHED', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USED', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=148,
  serialized_end=232,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTCONDITIONENUM_PRODUCTCONDITION)


_PRODUCTCONDITIONENUM = _descriptor.Descriptor(
  name='ProductConditionEnum',
  full_name='google.ads.googleads.v5.enums.ProductConditionEnum',
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
    _PRODUCTCONDITIONENUM_PRODUCTCONDITION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=232,
)

_PRODUCTCONDITIONENUM_PRODUCTCONDITION.containing_type = _PRODUCTCONDITIONENUM
DESCRIPTOR.message_types_by_name['ProductConditionEnum'] = _PRODUCTCONDITIONENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductConditionEnum = _reflection.GeneratedProtocolMessageType('ProductConditionEnum', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTCONDITIONENUM,
  '__module__' : 'google.ads.googleads_v5.proto.enums.product_condition_pb2'
  ,
  '__doc__': """Condition of a product offer.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.enums.ProductConditionEnum)
  })
_sym_db.RegisterMessage(ProductConditionEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
