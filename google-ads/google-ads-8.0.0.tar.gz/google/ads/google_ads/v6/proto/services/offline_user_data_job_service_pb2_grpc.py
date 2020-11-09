# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import offline_user_data_job_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_offline__user__data__job__pb2
from google.ads.google_ads.v6.proto.services import offline_user_data_job_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


class OfflineUserDataJobServiceStub(object):
    """Proto file describing the OfflineUserDataJobService.

    Service to manage offline user data jobs.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOfflineUserDataJob = channel.unary_unary(
                '/google.ads.googleads.v6.services.OfflineUserDataJobService/CreateOfflineUserDataJob',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.CreateOfflineUserDataJobRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.CreateOfflineUserDataJobResponse.FromString,
                )
        self.GetOfflineUserDataJob = channel.unary_unary(
                '/google.ads.googleads.v6.services.OfflineUserDataJobService/GetOfflineUserDataJob',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.GetOfflineUserDataJobRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_offline__user__data__job__pb2.OfflineUserDataJob.FromString,
                )
        self.AddOfflineUserDataJobOperations = channel.unary_unary(
                '/google.ads.googleads.v6.services.OfflineUserDataJobService/AddOfflineUserDataJobOperations',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.AddOfflineUserDataJobOperationsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.AddOfflineUserDataJobOperationsResponse.FromString,
                )
        self.RunOfflineUserDataJob = channel.unary_unary(
                '/google.ads.googleads.v6.services.OfflineUserDataJobService/RunOfflineUserDataJob',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.RunOfflineUserDataJobRequest.SerializeToString,
                response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
                )


class OfflineUserDataJobServiceServicer(object):
    """Proto file describing the OfflineUserDataJobService.

    Service to manage offline user data jobs.
    """

    def CreateOfflineUserDataJob(self, request, context):
        """Creates an offline user data job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOfflineUserDataJob(self, request, context):
        """Returns the offline user data job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddOfflineUserDataJobOperations(self, request, context):
        """Adds operations to the offline user data job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunOfflineUserDataJob(self, request, context):
        """Runs the offline user data job.

        When finished, the long running operation will contain the processing
        result or failure information, if any.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OfflineUserDataJobServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOfflineUserDataJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOfflineUserDataJob,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.CreateOfflineUserDataJobRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.CreateOfflineUserDataJobResponse.SerializeToString,
            ),
            'GetOfflineUserDataJob': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOfflineUserDataJob,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.GetOfflineUserDataJobRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_offline__user__data__job__pb2.OfflineUserDataJob.SerializeToString,
            ),
            'AddOfflineUserDataJobOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.AddOfflineUserDataJobOperations,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.AddOfflineUserDataJobOperationsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.AddOfflineUserDataJobOperationsResponse.SerializeToString,
            ),
            'RunOfflineUserDataJob': grpc.unary_unary_rpc_method_handler(
                    servicer.RunOfflineUserDataJob,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.RunOfflineUserDataJobRequest.FromString,
                    response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.OfflineUserDataJobService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OfflineUserDataJobService(object):
    """Proto file describing the OfflineUserDataJobService.

    Service to manage offline user data jobs.
    """

    @staticmethod
    def CreateOfflineUserDataJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.OfflineUserDataJobService/CreateOfflineUserDataJob',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.CreateOfflineUserDataJobRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.CreateOfflineUserDataJobResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOfflineUserDataJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.OfflineUserDataJobService/GetOfflineUserDataJob',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.GetOfflineUserDataJobRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_offline__user__data__job__pb2.OfflineUserDataJob.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddOfflineUserDataJobOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.OfflineUserDataJobService/AddOfflineUserDataJobOperations',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.AddOfflineUserDataJobOperationsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.AddOfflineUserDataJobOperationsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunOfflineUserDataJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.OfflineUserDataJobService/RunOfflineUserDataJob',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_offline__user__data__job__service__pb2.RunOfflineUserDataJobRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
