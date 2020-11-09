# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/enums/product_channel.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/enums/product_channel.proto',
  package='google.ads.googleads.v5.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v5.enumsB\023ProductChannelProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V5.Enums\312\002\035Google\\Ads\\GoogleAds\\V5\\Enums\352\002!Google::Ads::GoogleAds::V5::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9google/ads/googleads_v5/proto/enums/product_channel.proto\x12\x1dgoogle.ads.googleads.v5.enums\x1a\x1cgoogle/api/annotations.proto\"[\n\x12ProductChannelEnum\"E\n\x0eProductChannel\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06ONLINE\x10\x02\x12\t\n\x05LOCAL\x10\x03\x42\xe8\x01\n!com.google.ads.googleads.v5.enumsB\x13ProductChannelProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V5.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V5\\Enums\xea\x02!Google::Ads::GoogleAds::V5::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PRODUCTCHANNELENUM_PRODUCTCHANNEL = _descriptor.EnumDescriptor(
  name='ProductChannel',
  full_name='google.ads.googleads.v5.enums.ProductChannelEnum.ProductChannel',
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
      name='ONLINE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=144,
  serialized_end=213,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTCHANNELENUM_PRODUCTCHANNEL)


_PRODUCTCHANNELENUM = _descriptor.Descriptor(
  name='ProductChannelEnum',
  full_name='google.ads.googleads.v5.enums.ProductChannelEnum',
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
    _PRODUCTCHANNELENUM_PRODUCTCHANNEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=213,
)

_PRODUCTCHANNELENUM_PRODUCTCHANNEL.containing_type = _PRODUCTCHANNELENUM
DESCRIPTOR.message_types_by_name['ProductChannelEnum'] = _PRODUCTCHANNELENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductChannelEnum = _reflection.GeneratedProtocolMessageType('ProductChannelEnum', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTCHANNELENUM,
  '__module__' : 'google.ads.googleads_v5.proto.enums.product_channel_pb2'
  ,
  '__doc__': """Locality of a product offer.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.enums.ProductChannelEnum)
  })
_sym_db.RegisterMessage(ProductChannelEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
