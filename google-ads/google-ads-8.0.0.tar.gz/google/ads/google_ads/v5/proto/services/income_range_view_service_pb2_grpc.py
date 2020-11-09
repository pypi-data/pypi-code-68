# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.resources import income_range_view_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_income__range__view__pb2
from google.ads.google_ads.v5.proto.services import income_range_view_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_income__range__view__service__pb2


class IncomeRangeViewServiceStub(object):
    """Proto file describing the Income Range View service.

    Service to manage income range views.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetIncomeRangeView = channel.unary_unary(
                '/google.ads.googleads.v5.services.IncomeRangeViewService/GetIncomeRangeView',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_income__range__view__service__pb2.GetIncomeRangeViewRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_income__range__view__pb2.IncomeRangeView.FromString,
                )


class IncomeRangeViewServiceServicer(object):
    """Proto file describing the Income Range View service.

    Service to manage income range views.
    """

    def GetIncomeRangeView(self, request, context):
        """Returns the requested income range view in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IncomeRangeViewServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetIncomeRangeView': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIncomeRangeView,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_income__range__view__service__pb2.GetIncomeRangeViewRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_income__range__view__pb2.IncomeRangeView.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.IncomeRangeViewService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IncomeRangeViewService(object):
    """Proto file describing the Income Range View service.

    Service to manage income range views.
    """

    @staticmethod
    def GetIncomeRangeView(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.IncomeRangeViewService/GetIncomeRangeView',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_income__range__view__service__pb2.GetIncomeRangeViewRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_income__range__view__pb2.IncomeRangeView.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
