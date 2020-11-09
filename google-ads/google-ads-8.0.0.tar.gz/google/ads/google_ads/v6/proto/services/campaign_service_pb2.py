# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/services/campaign_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import response_content_type_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_response__content__type__pb2
from google.ads.google_ads.v6.proto.resources import campaign_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/services/campaign_service.proto',
  package='google.ads.googleads.v6.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v6.servicesB\024CampaignServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V6.Services\312\002 Google\\Ads\\GoogleAds\\V6\\Services\352\002$Google::Ads::GoogleAds::V6::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=google/ads/googleads_v6/proto/services/campaign_service.proto\x12 google.ads.googleads.v6.services\x1a?google/ads/googleads_v6/proto/enums/response_content_type.proto\x1a\x36google/ads/googleads_v6/proto/resources/campaign.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"V\n\x12GetCampaignRequest\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!googleads.googleapis.com/Campaign\"\x9b\x02\n\x16MutateCampaignsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12L\n\noperations\x18\x02 \x03(\x0b\x32\x33.google.ads.googleads.v6.services.CampaignOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12i\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v6.enums.ResponseContentTypeEnum.ResponseContentType\"\xe1\x01\n\x11\x43\x61mpaignOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12=\n\x06\x63reate\x18\x01 \x01(\x0b\x32+.google.ads.googleads.v6.resources.CampaignH\x00\x12=\n\x06update\x18\x02 \x01(\x0b\x32+.google.ads.googleads.v6.resources.CampaignH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x95\x01\n\x17MutateCampaignsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12G\n\x07results\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v6.services.MutateCampaignResult\"l\n\x14MutateCampaignResult\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12=\n\x08\x63\x61mpaign\x18\x02 \x01(\x0b\x32+.google.ads.googleads.v6.resources.Campaign2\xc3\x03\n\x0f\x43\x61mpaignService\x12\xb5\x01\n\x0bGetCampaign\x12\x34.google.ads.googleads.v6.services.GetCampaignRequest\x1a+.google.ads.googleads.v6.resources.Campaign\"C\x82\xd3\xe4\x93\x02-\x12+/v6/{resource_name=customers/*/campaigns/*}\xda\x41\rresource_name\x12\xda\x01\n\x0fMutateCampaigns\x12\x38.google.ads.googleads.v6.services.MutateCampaignsRequest\x1a\x39.google.ads.googleads.v6.services.MutateCampaignsResponse\"R\x82\xd3\xe4\x93\x02\x33\"./v6/customers/{customer_id=*}/campaigns:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xfb\x01\n$com.google.ads.googleads.v6.servicesB\x14\x43\x61mpaignServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V6.Services\xca\x02 Google\\Ads\\GoogleAds\\V6\\Services\xea\x02$Google::Ads::GoogleAds::V6::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_response__content__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETCAMPAIGNREQUEST = _descriptor.Descriptor(
  name='GetCampaignRequest',
  full_name='google.ads.googleads.v6.services.GetCampaignRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.GetCampaignRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A#\n!googleads.googleapis.com/Campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=394,
  serialized_end=480,
)


_MUTATECAMPAIGNSREQUEST = _descriptor.Descriptor(
  name='MutateCampaignsRequest',
  full_name='google.ads.googleads.v6.services.MutateCampaignsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v6.services.MutateCampaignsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v6.services.MutateCampaignsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v6.services.MutateCampaignsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v6.services.MutateCampaignsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_content_type', full_name='google.ads.googleads.v6.services.MutateCampaignsRequest.response_content_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=483,
  serialized_end=766,
)


_CAMPAIGNOPERATION = _descriptor.Descriptor(
  name='CampaignOperation',
  full_name='google.ads.googleads.v6.services.CampaignOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v6.services.CampaignOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v6.services.CampaignOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v6.services.CampaignOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v6.services.CampaignOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v6.services.CampaignOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=769,
  serialized_end=994,
)


_MUTATECAMPAIGNSRESPONSE = _descriptor.Descriptor(
  name='MutateCampaignsResponse',
  full_name='google.ads.googleads.v6.services.MutateCampaignsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v6.services.MutateCampaignsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v6.services.MutateCampaignsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=997,
  serialized_end=1146,
)


_MUTATECAMPAIGNRESULT = _descriptor.Descriptor(
  name='MutateCampaignResult',
  full_name='google.ads.googleads.v6.services.MutateCampaignResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.MutateCampaignResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v6.services.MutateCampaignResult.campaign', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1148,
  serialized_end=1256,
)

_MUTATECAMPAIGNSREQUEST.fields_by_name['operations'].message_type = _CAMPAIGNOPERATION
_MUTATECAMPAIGNSREQUEST.fields_by_name['response_content_type'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_response__content__type__pb2._RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE
_CAMPAIGNOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CAMPAIGNOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__pb2._CAMPAIGN
_CAMPAIGNOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__pb2._CAMPAIGN
_CAMPAIGNOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNOPERATION.fields_by_name['create'])
_CAMPAIGNOPERATION.fields_by_name['create'].containing_oneof = _CAMPAIGNOPERATION.oneofs_by_name['operation']
_CAMPAIGNOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNOPERATION.fields_by_name['update'])
_CAMPAIGNOPERATION.fields_by_name['update'].containing_oneof = _CAMPAIGNOPERATION.oneofs_by_name['operation']
_CAMPAIGNOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNOPERATION.fields_by_name['remove'])
_CAMPAIGNOPERATION.fields_by_name['remove'].containing_oneof = _CAMPAIGNOPERATION.oneofs_by_name['operation']
_MUTATECAMPAIGNSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATECAMPAIGNSRESPONSE.fields_by_name['results'].message_type = _MUTATECAMPAIGNRESULT
_MUTATECAMPAIGNRESULT.fields_by_name['campaign'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__pb2._CAMPAIGN
DESCRIPTOR.message_types_by_name['GetCampaignRequest'] = _GETCAMPAIGNREQUEST
DESCRIPTOR.message_types_by_name['MutateCampaignsRequest'] = _MUTATECAMPAIGNSREQUEST
DESCRIPTOR.message_types_by_name['CampaignOperation'] = _CAMPAIGNOPERATION
DESCRIPTOR.message_types_by_name['MutateCampaignsResponse'] = _MUTATECAMPAIGNSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCampaignResult'] = _MUTATECAMPAIGNRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCampaignRequest = _reflection.GeneratedProtocolMessageType('GetCampaignRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCAMPAIGNREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.campaign_service_pb2'
  ,
  '__doc__': """Request message for [CampaignService.GetCampaign][google.ads.googleads
  .v6.services.CampaignService.GetCampaign].
  
  Attributes:
      resource_name:
          Required. The resource name of the campaign to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.GetCampaignRequest)
  })
_sym_db.RegisterMessage(GetCampaignRequest)

MutateCampaignsRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNSREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.campaign_service_pb2'
  ,
  '__doc__': """Request message for [CampaignService.MutateCampaigns][google.ads.googl
  eads.v6.services.CampaignService.MutateCampaigns].
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose campaigns are being
          modified.
      operations:
          Required. The list of operations to perform on individual
          campaigns.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
      response_content_type:
          The response content type setting. Determines whether the
          mutable resource or just the resource name should be returned
          post mutation.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCampaignsRequest)
  })
_sym_db.RegisterMessage(MutateCampaignsRequest)

CampaignOperation = _reflection.GeneratedProtocolMessageType('CampaignOperation', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNOPERATION,
  '__module__' : 'google.ads.googleads_v6.proto.services.campaign_service_pb2'
  ,
  '__doc__': """A single operation (create, update, remove) on a campaign.
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          campaign.
      update:
          Update operation: The campaign is expected to have a valid
          resource name.
      remove:
          Remove operation: A resource name for the removed campaign is
          expected, in this format:
          ``customers/{customer_id}/campaigns/{campaign_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.CampaignOperation)
  })
_sym_db.RegisterMessage(CampaignOperation)

MutateCampaignsResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNSRESPONSE,
  '__module__' : 'google.ads.googleads_v6.proto.services.campaign_service_pb2'
  ,
  '__doc__': """Response message for campaign mutate.
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCampaignsResponse)
  })
_sym_db.RegisterMessage(MutateCampaignsResponse)

MutateCampaignResult = _reflection.GeneratedProtocolMessageType('MutateCampaignResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNRESULT,
  '__module__' : 'google.ads.googleads_v6.proto.services.campaign_service_pb2'
  ,
  '__doc__': """The result for the campaign mutate.
  
  Attributes:
      resource_name:
          Returned for successful operations.
      campaign:
          The mutated campaign with only mutable fields after mutate.
          The field will only be returned when response\_content\_type
          is set to "MUTABLE\_RESOURCE".
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCampaignResult)
  })
_sym_db.RegisterMessage(MutateCampaignResult)


DESCRIPTOR._options = None
_GETCAMPAIGNREQUEST.fields_by_name['resource_name']._options = None
_MUTATECAMPAIGNSREQUEST.fields_by_name['customer_id']._options = None
_MUTATECAMPAIGNSREQUEST.fields_by_name['operations']._options = None

_CAMPAIGNSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignService',
  full_name='google.ads.googleads.v6.services.CampaignService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=1259,
  serialized_end=1710,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCampaign',
    full_name='google.ads.googleads.v6.services.CampaignService.GetCampaign',
    index=0,
    containing_service=None,
    input_type=_GETCAMPAIGNREQUEST,
    output_type=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__pb2._CAMPAIGN,
    serialized_options=b'\202\323\344\223\002-\022+/v6/{resource_name=customers/*/campaigns/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateCampaigns',
    full_name='google.ads.googleads.v6.services.CampaignService.MutateCampaigns',
    index=1,
    containing_service=None,
    input_type=_MUTATECAMPAIGNSREQUEST,
    output_type=_MUTATECAMPAIGNSRESPONSE,
    serialized_options=b'\202\323\344\223\0023\"./v6/customers/{customer_id=*}/campaigns:mutate:\001*\332A\026customer_id,operations',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNSERVICE)

DESCRIPTOR.services_by_name['CampaignService'] = _CAMPAIGNSERVICE

# @@protoc_insertion_point(module_scope)
