# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/resources/geographic_view.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import geo_targeting_type_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_geo__targeting__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/resources/geographic_view.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\023GeographicViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=google/ads/googleads_v6/proto/resources/geographic_view.proto\x12!google.ads.googleads.v6.resources\x1a<google/ads/googleads_v6/proto/enums/geo_targeting_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xf9\x02\n\x0eGeographicView\x12\x46\n\rresource_name\x18\x01 \x01(\tB/\xe0\x41\x03\xfa\x41)\n\'googleads.googleapis.com/GeographicView\x12`\n\rlocation_type\x18\x03 \x01(\x0e\x32\x44.google.ads.googleads.v6.enums.GeoTargetingTypeEnum.GeoTargetingTypeB\x03\xe0\x41\x03\x12&\n\x14\x63ountry_criterion_id\x18\x05 \x01(\x03\x42\x03\xe0\x41\x03H\x00\x88\x01\x01:|\xea\x41y\n\'googleads.googleapis.com/GeographicView\x12Ncustomers/{customer_id}/geographicViews/{country_criterion_id}~{location_type}B\x17\n\x15_country_criterion_idB\x80\x02\n%com.google.ads.googleads.v6.resourcesB\x13GeographicViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_geo__targeting__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GEOGRAPHICVIEW = _descriptor.Descriptor(
  name='GeographicView',
  full_name='google.ads.googleads.v6.resources.GeographicView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.GeographicView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A)\n\'googleads.googleapis.com/GeographicView', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location_type', full_name='google.ads.googleads.v6.resources.GeographicView.location_type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_criterion_id', full_name='google.ads.googleads.v6.resources.GeographicView.country_criterion_id', index=2,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Ay\n\'googleads.googleapis.com/GeographicView\022Ncustomers/{customer_id}/geographicViews/{country_criterion_id}~{location_type}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_country_criterion_id', full_name='google.ads.googleads.v6.resources.GeographicView._country_criterion_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=253,
  serialized_end=630,
)

_GEOGRAPHICVIEW.fields_by_name['location_type'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_geo__targeting__type__pb2._GEOTARGETINGTYPEENUM_GEOTARGETINGTYPE
_GEOGRAPHICVIEW.oneofs_by_name['_country_criterion_id'].fields.append(
  _GEOGRAPHICVIEW.fields_by_name['country_criterion_id'])
_GEOGRAPHICVIEW.fields_by_name['country_criterion_id'].containing_oneof = _GEOGRAPHICVIEW.oneofs_by_name['_country_criterion_id']
DESCRIPTOR.message_types_by_name['GeographicView'] = _GEOGRAPHICVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeographicView = _reflection.GeneratedProtocolMessageType('GeographicView', (_message.Message,), {
  'DESCRIPTOR' : _GEOGRAPHICVIEW,
  '__module__' : 'google.ads.googleads_v6.proto.resources.geographic_view_pb2'
  ,
  '__doc__': """A geographic view.  Geographic View includes all metrics aggregated at
  the country level, one row per country. It reports metrics at either
  actual physical location of the user or an area of interest. If other
  segment fields are used, you may get more than one row per country.
  
  Attributes:
      resource_name:
          Output only. The resource name of the geographic view.
          Geographic view resource names have the form:  ``customers/{cu
          stomer_id}/geographicViews/{country_criterion_id}~{location_ty
          pe}``
      location_type:
          Output only. Type of the geo targeting of the campaign.
      country_criterion_id:
          Output only. Criterion Id for the country.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.GeographicView)
  })
_sym_db.RegisterMessage(GeographicView)


DESCRIPTOR._options = None
_GEOGRAPHICVIEW.fields_by_name['resource_name']._options = None
_GEOGRAPHICVIEW.fields_by_name['location_type']._options = None
_GEOGRAPHICVIEW.fields_by_name['country_criterion_id']._options = None
_GEOGRAPHICVIEW._options = None
# @@protoc_insertion_point(module_scope)
