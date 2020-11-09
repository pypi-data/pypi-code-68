# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/services/google_ads_field_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.resources import google_ads_field_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_google__ads__field__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/services/google_ads_field_service.proto',
  package='google.ads.googleads.v4.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v4.servicesB\032GoogleAdsFieldServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V4.Services\312\002 Google\\Ads\\GoogleAds\\V4\\Services\352\002$Google::Ads::GoogleAds::V4::Services'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v4/proto/services/google_ads_field_service.proto\x12 google.ads.googleads.v4.services\x1a>google/ads/googleads_v4/proto/resources/google_ads_field.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"b\n\x18GetGoogleAdsFieldRequest\x12\x46\n\rresource_name\x18\x01 \x01(\tB/\xe0\x41\x02\xfa\x41)\n\'googleads.googleapis.com/GoogleAdsField\"Y\n\x1cSearchGoogleAdsFieldsRequest\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\"\x99\x01\n\x1dSearchGoogleAdsFieldsResponse\x12\x42\n\x07results\x18\x01 \x03(\x0b\x32\x31.google.ads.googleads.v4.resources.GoogleAdsField\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x1b\n\x13total_results_count\x18\x03 \x01(\x03\x32\xc2\x03\n\x15GoogleAdsFieldService\x12\xc1\x01\n\x11GetGoogleAdsField\x12:.google.ads.googleads.v4.services.GetGoogleAdsFieldRequest\x1a\x31.google.ads.googleads.v4.resources.GoogleAdsField\"=\x82\xd3\xe4\x93\x02\'\x12%/v4/{resource_name=googleAdsFields/*}\xda\x41\rresource_name\x12\xc7\x01\n\x15SearchGoogleAdsFields\x12>.google.ads.googleads.v4.services.SearchGoogleAdsFieldsRequest\x1a?.google.ads.googleads.v4.services.SearchGoogleAdsFieldsResponse\"-\x82\xd3\xe4\x93\x02\x1f\"\x1a/v4/googleAdsFields:search:\x01*\xda\x41\x05query\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x81\x02\n$com.google.ads.googleads.v4.servicesB\x1aGoogleAdsFieldServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V4.Services\xca\x02 Google\\Ads\\GoogleAds\\V4\\Services\xea\x02$Google::Ads::GoogleAds::V4::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_google__ads__field__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETGOOGLEADSFIELDREQUEST = _descriptor.Descriptor(
  name='GetGoogleAdsFieldRequest',
  full_name='google.ads.googleads.v4.services.GetGoogleAdsFieldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.GetGoogleAdsFieldRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A)\n\'googleads.googleapis.com/GoogleAdsField'), file=DESCRIPTOR),
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
  serialized_start=286,
  serialized_end=384,
)


_SEARCHGOOGLEADSFIELDSREQUEST = _descriptor.Descriptor(
  name='SearchGoogleAdsFieldsRequest',
  full_name='google.ads.googleads.v4.services.SearchGoogleAdsFieldsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='google.ads.googleads.v4.services.SearchGoogleAdsFieldsRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.ads.googleads.v4.services.SearchGoogleAdsFieldsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.ads.googleads.v4.services.SearchGoogleAdsFieldsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=386,
  serialized_end=475,
)


_SEARCHGOOGLEADSFIELDSRESPONSE = _descriptor.Descriptor(
  name='SearchGoogleAdsFieldsResponse',
  full_name='google.ads.googleads.v4.services.SearchGoogleAdsFieldsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v4.services.SearchGoogleAdsFieldsResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.ads.googleads.v4.services.SearchGoogleAdsFieldsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_results_count', full_name='google.ads.googleads.v4.services.SearchGoogleAdsFieldsResponse.total_results_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=478,
  serialized_end=631,
)

_SEARCHGOOGLEADSFIELDSRESPONSE.fields_by_name['results'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_google__ads__field__pb2._GOOGLEADSFIELD
DESCRIPTOR.message_types_by_name['GetGoogleAdsFieldRequest'] = _GETGOOGLEADSFIELDREQUEST
DESCRIPTOR.message_types_by_name['SearchGoogleAdsFieldsRequest'] = _SEARCHGOOGLEADSFIELDSREQUEST
DESCRIPTOR.message_types_by_name['SearchGoogleAdsFieldsResponse'] = _SEARCHGOOGLEADSFIELDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetGoogleAdsFieldRequest = _reflection.GeneratedProtocolMessageType('GetGoogleAdsFieldRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETGOOGLEADSFIELDREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.google_ads_field_service_pb2'
  ,
  __doc__ = """Request message for
  [GoogleAdsFieldService.GetGoogleAdsField][google.ads.googleads.v4.services.GoogleAdsFieldService.GetGoogleAdsField].
  
  
  Attributes:
      resource_name:
          Required. The resource name of the field to get.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.GetGoogleAdsFieldRequest)
  ))
_sym_db.RegisterMessage(GetGoogleAdsFieldRequest)

SearchGoogleAdsFieldsRequest = _reflection.GeneratedProtocolMessageType('SearchGoogleAdsFieldsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHGOOGLEADSFIELDSREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.google_ads_field_service_pb2'
  ,
  __doc__ = """Request message for
  [GoogleAdsFieldService.SearchGoogleAdsFields][google.ads.googleads.v4.services.GoogleAdsFieldService.SearchGoogleAdsFields].
  
  
  Attributes:
      query:
          Required. The query string.
      page_token:
          Token of the page to retrieve. If not specified, the first
          page of results will be returned. Use the value obtained from
          ``next_page_token`` in the previous response in order to
          request the next page of results.
      page_size:
          Number of elements to retrieve in a single page. When too
          large a page is requested, the server may decide to further
          limit the number of returned resources.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.SearchGoogleAdsFieldsRequest)
  ))
_sym_db.RegisterMessage(SearchGoogleAdsFieldsRequest)

SearchGoogleAdsFieldsResponse = _reflection.GeneratedProtocolMessageType('SearchGoogleAdsFieldsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHGOOGLEADSFIELDSRESPONSE,
  __module__ = 'google.ads.googleads_v4.proto.services.google_ads_field_service_pb2'
  ,
  __doc__ = """Response message for
  [GoogleAdsFieldService.SearchGoogleAdsFields][google.ads.googleads.v4.services.GoogleAdsFieldService.SearchGoogleAdsFields].
  
  
  Attributes:
      results:
          The list of fields that matched the query.
      next_page_token:
          Pagination token used to retrieve the next page of results.
          Pass the content of this string as the ``page_token``
          attribute of the next request. ``next_page_token`` is not
          returned for the last page.
      total_results_count:
          Total number of results that match the query ignoring the
          LIMIT clause.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.SearchGoogleAdsFieldsResponse)
  ))
_sym_db.RegisterMessage(SearchGoogleAdsFieldsResponse)


DESCRIPTOR._options = None
_GETGOOGLEADSFIELDREQUEST.fields_by_name['resource_name']._options = None
_SEARCHGOOGLEADSFIELDSREQUEST.fields_by_name['query']._options = None

_GOOGLEADSFIELDSERVICE = _descriptor.ServiceDescriptor(
  name='GoogleAdsFieldService',
  full_name='google.ads.googleads.v4.services.GoogleAdsFieldService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=634,
  serialized_end=1084,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetGoogleAdsField',
    full_name='google.ads.googleads.v4.services.GoogleAdsFieldService.GetGoogleAdsField',
    index=0,
    containing_service=None,
    input_type=_GETGOOGLEADSFIELDREQUEST,
    output_type=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_google__ads__field__pb2._GOOGLEADSFIELD,
    serialized_options=_b('\202\323\344\223\002\'\022%/v4/{resource_name=googleAdsFields/*}\332A\rresource_name'),
  ),
  _descriptor.MethodDescriptor(
    name='SearchGoogleAdsFields',
    full_name='google.ads.googleads.v4.services.GoogleAdsFieldService.SearchGoogleAdsFields',
    index=1,
    containing_service=None,
    input_type=_SEARCHGOOGLEADSFIELDSREQUEST,
    output_type=_SEARCHGOOGLEADSFIELDSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\037\"\032/v4/googleAdsFields:search:\001*\332A\005query'),
  ),
])
_sym_db.RegisterServiceDescriptor(_GOOGLEADSFIELDSERVICE)

DESCRIPTOR.services_by_name['GoogleAdsFieldService'] = _GOOGLEADSFIELDSERVICE

# @@protoc_insertion_point(module_scope)
