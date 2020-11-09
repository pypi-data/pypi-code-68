# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/services/currency_constant_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.resources import currency_constant_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_currency__constant__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/services/currency_constant_service.proto',
  package='google.ads.googleads.v6.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v6.servicesB\034CurrencyConstantServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V6.Services\312\002 Google\\Ads\\GoogleAds\\V6\\Services\352\002$Google::Ads::GoogleAds::V6::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nFgoogle/ads/googleads_v6/proto/services/currency_constant_service.proto\x12 google.ads.googleads.v6.services\x1a?google/ads/googleads_v6/proto/resources/currency_constant.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"f\n\x1aGetCurrencyConstantRequest\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0\x41\x02\xfa\x41+\n)googleads.googleapis.com/CurrencyConstant2\x82\x02\n\x17\x43urrencyConstantService\x12\xc9\x01\n\x13GetCurrencyConstant\x12<.google.ads.googleads.v6.services.GetCurrencyConstantRequest\x1a\x33.google.ads.googleads.v6.resources.CurrencyConstant\"?\x82\xd3\xe4\x93\x02)\x12\'/v6/{resource_name=currencyConstants/*}\xda\x41\rresource_name\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x83\x02\n$com.google.ads.googleads.v6.servicesB\x1c\x43urrencyConstantServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V6.Services\xca\x02 Google\\Ads\\GoogleAds\\V6\\Services\xea\x02$Google::Ads::GoogleAds::V6::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_currency__constant__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETCURRENCYCONSTANTREQUEST = _descriptor.Descriptor(
  name='GetCurrencyConstantRequest',
  full_name='google.ads.googleads.v6.services.GetCurrencyConstantRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.GetCurrencyConstantRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A+\n)googleads.googleapis.com/CurrencyConstant', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=390,
)

DESCRIPTOR.message_types_by_name['GetCurrencyConstantRequest'] = _GETCURRENCYCONSTANTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCurrencyConstantRequest = _reflection.GeneratedProtocolMessageType('GetCurrencyConstantRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCURRENCYCONSTANTREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.currency_constant_service_pb2'
  ,
  '__doc__': """Request message for [CurrencyConstantService.GetCurrencyConstant][goog
  le.ads.googleads.v6.services.CurrencyConstantService.GetCurrencyConsta
  nt].
  
  Attributes:
      resource_name:
          Required. Resource name of the currency constant to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.GetCurrencyConstantRequest)
  })
_sym_db.RegisterMessage(GetCurrencyConstantRequest)


DESCRIPTOR._options = None
_GETCURRENCYCONSTANTREQUEST.fields_by_name['resource_name']._options = None

_CURRENCYCONSTANTSERVICE = _descriptor.ServiceDescriptor(
  name='CurrencyConstantService',
  full_name='google.ads.googleads.v6.services.CurrencyConstantService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=393,
  serialized_end=651,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCurrencyConstant',
    full_name='google.ads.googleads.v6.services.CurrencyConstantService.GetCurrencyConstant',
    index=0,
    containing_service=None,
    input_type=_GETCURRENCYCONSTANTREQUEST,
    output_type=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_currency__constant__pb2._CURRENCYCONSTANT,
    serialized_options=b'\202\323\344\223\002)\022\'/v6/{resource_name=currencyConstants/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CURRENCYCONSTANTSERVICE)

DESCRIPTOR.services_by_name['CurrencyConstantService'] = _CURRENCYCONSTANTSERVICE

# @@protoc_insertion_point(module_scope)
