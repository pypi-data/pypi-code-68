# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.services import google_ads_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2


class GoogleAdsServiceStub(object):
    """Proto file describing the GoogleAdsService.

    Service to fetch data and metrics across resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
                '/google.ads.googleads.v6.services.GoogleAdsService/Search',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsResponse.FromString,
                )
        self.SearchStream = channel.unary_stream(
                '/google.ads.googleads.v6.services.GoogleAdsService/SearchStream',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsStreamRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsStreamResponse.FromString,
                )
        self.Mutate = channel.unary_unary(
                '/google.ads.googleads.v6.services.GoogleAdsService/Mutate',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.MutateGoogleAdsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.MutateGoogleAdsResponse.FromString,
                )


class GoogleAdsServiceServicer(object):
    """Proto file describing the GoogleAdsService.

    Service to fetch data and metrics across resources.
    """

    def Search(self, request, context):
        """Returns all rows that match the search query.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchStream(self, request, context):
        """Returns all rows that match the search stream query.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Mutate(self, request, context):
        """Creates, updates, or removes resources. This method supports atomic
        transactions with multiple types of resources. For example, you can
        atomically create a campaign and a campaign budget, or perform up to
        thousands of mutates atomically.

        This method is essentially a wrapper around a series of mutate methods. The
        only features it offers over calling those methods directly are:

        - Atomic transactions
        - Temp resource names (described below)
        - Somewhat reduced latency over making a series of mutate calls

        Note: Only resources that support atomic transactions are included, so this
        method can't replace all calls to individual services.

        ## Atomic Transaction Benefits

        Atomicity makes error handling much easier. If you're making a series of
        changes and one fails, it can leave your account in an inconsistent state.
        With atomicity, you either reach the desired state directly, or the request
        fails and you can retry.

        ## Temp Resource Names

        Temp resource names are a special type of resource name used to create a
        resource and reference that resource in the same request. For example, if a
        campaign budget is created with `resource_name` equal to
        `customers/123/campaignBudgets/-1`, that resource name can be reused in
        the `Campaign.budget` field in the same request. That way, the two
        resources are created and linked atomically.

        To create a temp resource name, put a negative number in the part of the
        name that the server would normally allocate.

        Note:

        - Resources must be created with a temp name before the name can be reused.
        For example, the previous CampaignBudget+Campaign example would fail if
        the mutate order was reversed.
        - Temp names are not remembered across requests.
        - There's no limit to the number of temp names in a request.
        - Each temp name must use a unique negative number, even if the resource
        types differ.

        ## Latency

        It's important to group mutates by resource type or the request may time
        out and fail. Latency is roughly equal to a series of calls to individual
        mutate methods, where each change in resource type is a new call. For
        example, mutating 10 campaigns then 10 ad groups is like 2 calls, while
        mutating 1 campaign, 1 ad group, 1 campaign, 1 ad group is like 4 calls.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GoogleAdsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsResponse.SerializeToString,
            ),
            'SearchStream': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchStream,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsStreamRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsStreamResponse.SerializeToString,
            ),
            'Mutate': grpc.unary_unary_rpc_method_handler(
                    servicer.Mutate,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.MutateGoogleAdsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.MutateGoogleAdsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.GoogleAdsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GoogleAdsService(object):
    """Proto file describing the GoogleAdsService.

    Service to fetch data and metrics across resources.
    """

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.GoogleAdsService/Search',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/google.ads.googleads.v6.services.GoogleAdsService/SearchStream',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsStreamRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsStreamResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Mutate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.GoogleAdsService/Mutate',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.MutateGoogleAdsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__service__pb2.MutateGoogleAdsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
