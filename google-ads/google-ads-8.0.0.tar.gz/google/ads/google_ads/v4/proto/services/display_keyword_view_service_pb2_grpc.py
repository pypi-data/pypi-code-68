# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import display_keyword_view_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_display__keyword__view__pb2
from google.ads.google_ads.v4.proto.services import display_keyword_view_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_display__keyword__view__service__pb2


class DisplayKeywordViewServiceStub(object):
  """Proto file describing the Display Keyword View service.

  Service to manage display keyword views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetDisplayKeywordView = channel.unary_unary(
        '/google.ads.googleads.v4.services.DisplayKeywordViewService/GetDisplayKeywordView',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_display__keyword__view__service__pb2.GetDisplayKeywordViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_display__keyword__view__pb2.DisplayKeywordView.FromString,
        )


class DisplayKeywordViewServiceServicer(object):
  """Proto file describing the Display Keyword View service.

  Service to manage display keyword views.
  """

  def GetDisplayKeywordView(self, request, context):
    """Returns the requested display keyword view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DisplayKeywordViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetDisplayKeywordView': grpc.unary_unary_rpc_method_handler(
          servicer.GetDisplayKeywordView,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_display__keyword__view__service__pb2.GetDisplayKeywordViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_display__keyword__view__pb2.DisplayKeywordView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.DisplayKeywordViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
