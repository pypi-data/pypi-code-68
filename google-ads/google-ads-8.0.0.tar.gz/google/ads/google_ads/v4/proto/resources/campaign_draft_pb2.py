# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/resources/campaign_draft.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.enums import campaign_draft_status_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_campaign__draft__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/resources/campaign_draft.proto',
  package='google.ads.googleads.v4.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v4.resourcesB\022CampaignDraftProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V4.Resources\312\002!Google\\Ads\\GoogleAds\\V4\\Resources\352\002%Google::Ads::GoogleAds::V4::Resources'),
  serialized_pb=_b('\n<google/ads/googleads_v4/proto/resources/campaign_draft.proto\x12!google.ads.googleads.v4.resources\x1a?google/ads/googleads_v4/proto/enums/campaign_draft_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xbf\x05\n\rCampaignDraft\x12\x45\n\rresource_name\x18\x01 \x01(\tB.\xe0\x41\x05\xfa\x41(\n&googleads.googleapis.com/CampaignDraft\x12\x32\n\x08\x64raft_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12^\n\rbase_campaign\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB)\xe0\x41\x05\xfa\x41#\n!googleads.googleapis.com/Campaign\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12_\n\x0e\x64raft_campaign\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueB)\xe0\x41\x03\xfa\x41#\n!googleads.googleapis.com/Campaign\x12_\n\x06status\x18\x06 \x01(\x0e\x32J.google.ads.googleads.v4.enums.CampaignDraftStatusEnum.CampaignDraftStatusB\x03\xe0\x41\x03\x12?\n\x16has_experiment_running\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x03\xe0\x41\x03\x12\x41\n\x16long_running_operation\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03:a\xea\x41^\n&googleads.googleapis.com/CampaignDraft\x12\x34\x63ustomers/{customer}/campaignDrafts/{campaign_draft}B\xff\x01\n%com.google.ads.googleads.v4.resourcesB\x12\x43\x61mpaignDraftProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V4.Resources\xca\x02!Google\\Ads\\GoogleAds\\V4\\Resources\xea\x02%Google::Ads::GoogleAds::V4::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_campaign__draft__status__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNDRAFT = _descriptor.Descriptor(
  name='CampaignDraft',
  full_name='google.ads.googleads.v4.resources.CampaignDraft',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.resources.CampaignDraft.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A(\n&googleads.googleapis.com/CampaignDraft'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='draft_id', full_name='google.ads.googleads.v4.resources.CampaignDraft.draft_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_campaign', full_name='google.ads.googleads.v4.resources.CampaignDraft.base_campaign', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A#\n!googleads.googleapis.com/Campaign'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v4.resources.CampaignDraft.name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='draft_campaign', full_name='google.ads.googleads.v4.resources.CampaignDraft.draft_campaign', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003\372A#\n!googleads.googleapis.com/Campaign'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v4.resources.CampaignDraft.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_experiment_running', full_name='google.ads.googleads.v4.resources.CampaignDraft.has_experiment_running', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_running_operation', full_name='google.ads.googleads.v4.resources.CampaignDraft.long_running_operation', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352A^\n&googleads.googleapis.com/CampaignDraft\0224customers/{customer}/campaignDrafts/{campaign_draft}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=990,
)

_CAMPAIGNDRAFT.fields_by_name['draft_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CAMPAIGNDRAFT.fields_by_name['base_campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNDRAFT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNDRAFT.fields_by_name['draft_campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNDRAFT.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_campaign__draft__status__pb2._CAMPAIGNDRAFTSTATUSENUM_CAMPAIGNDRAFTSTATUS
_CAMPAIGNDRAFT.fields_by_name['has_experiment_running'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CAMPAIGNDRAFT.fields_by_name['long_running_operation'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['CampaignDraft'] = _CAMPAIGNDRAFT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignDraft = _reflection.GeneratedProtocolMessageType('CampaignDraft', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNDRAFT,
  __module__ = 'google.ads.googleads_v4.proto.resources.campaign_draft_pb2'
  ,
  __doc__ = """A campaign draft.
  
  
  Attributes:
      resource_name:
          Immutable. The resource name of the campaign draft. Campaign
          draft resource names have the form:  ``customers/{customer_id}
          /campaignDrafts/{base_campaign_id}~{draft_id}``
      draft_id:
          Output only. The ID of the draft.  This field is read-only.
      base_campaign:
          Immutable. The base campaign to which the draft belongs.
      name:
          The name of the campaign draft.  This field is required and
          should not be empty when creating new campaign drafts.  It
          must not contain any null (code point 0x0), NL line feed (code
          point 0xA) or carriage return (code point 0xD) characters.
      draft_campaign:
          Output only. Resource name of the Campaign that results from
          overlaying the draft changes onto the base campaign.  This
          field is read-only.
      status:
          Output only. The status of the campaign draft. This field is
          read-only.  When a new campaign draft is added, the status
          defaults to PROPOSED.
      has_experiment_running:
          Output only. Whether there is an experiment based on this
          draft currently serving.
      long_running_operation:
          Output only. The resource name of the long-running operation
          that can be used to poll for completion of draft promotion.
          This is only set if the draft promotion is in progress or
          finished.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.resources.CampaignDraft)
  ))
_sym_db.RegisterMessage(CampaignDraft)


DESCRIPTOR._options = None
_CAMPAIGNDRAFT.fields_by_name['resource_name']._options = None
_CAMPAIGNDRAFT.fields_by_name['draft_id']._options = None
_CAMPAIGNDRAFT.fields_by_name['base_campaign']._options = None
_CAMPAIGNDRAFT.fields_by_name['draft_campaign']._options = None
_CAMPAIGNDRAFT.fields_by_name['status']._options = None
_CAMPAIGNDRAFT.fields_by_name['has_experiment_running']._options = None
_CAMPAIGNDRAFT.fields_by_name['long_running_operation']._options = None
_CAMPAIGNDRAFT._options = None
# @@protoc_insertion_point(module_scope)
