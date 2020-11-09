# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/resources/parental_status_view.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/resources/parental_status_view.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\027ParentalStatusViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nBgoogle/ads/googleads_v6/proto/resources/parental_status_view.proto\x12!google.ads.googleads.v6.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xdc\x01\n\x12ParentalStatusView\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0\x41\x03\xfa\x41-\n+googleads.googleapis.com/ParentalStatusView:z\xea\x41w\n+googleads.googleapis.com/ParentalStatusView\x12Hcustomers/{customer_id}/parentalStatusViews/{ad_group_id}~{criterion_id}B\x84\x02\n%com.google.ads.googleads.v6.resourcesB\x17ParentalStatusViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_PARENTALSTATUSVIEW = _descriptor.Descriptor(
  name='ParentalStatusView',
  full_name='google.ads.googleads.v6.resources.ParentalStatusView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.ParentalStatusView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A-\n+googleads.googleapis.com/ParentalStatusView', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Aw\n+googleads.googleapis.com/ParentalStatusView\022Hcustomers/{customer_id}/parentalStatusViews/{ad_group_id}~{criterion_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=416,
)

DESCRIPTOR.message_types_by_name['ParentalStatusView'] = _PARENTALSTATUSVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParentalStatusView = _reflection.GeneratedProtocolMessageType('ParentalStatusView', (_message.Message,), {
  'DESCRIPTOR' : _PARENTALSTATUSVIEW,
  '__module__' : 'google.ads.googleads_v6.proto.resources.parental_status_view_pb2'
  ,
  '__doc__': """A parental status view.
  
  Attributes:
      resource_name:
          Output only. The resource name of the parental status view.
          Parental Status view resource names have the form:  ``customer
          s/{customer_id}/parentalStatusViews/{ad_group_id}~{criterion_i
          d}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.ParentalStatusView)
  })
_sym_db.RegisterMessage(ParentalStatusView)


DESCRIPTOR._options = None
_PARENTALSTATUSVIEW.fields_by_name['resource_name']._options = None
_PARENTALSTATUSVIEW._options = None
# @@protoc_insertion_point(module_scope)
