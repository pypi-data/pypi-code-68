# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.aiplatform_v1beta1.types import endpoint
from google.cloud.aiplatform_v1beta1.types import endpoint as gca_endpoint
from google.cloud.aiplatform_v1beta1.types import endpoint_service
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import EndpointServiceTransport, DEFAULT_CLIENT_INFO


class EndpointServiceGrpcTransport(EndpointServiceTransport):
    """gRPC backend transport for EndpointService.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "aiplatform.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._ssl_channel_credentials = ssl_channel_credentials

        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        elif api_mtls_endpoint:
            warnings.warn(
                "api_mtls_endpoint and client_cert_source are deprecated",
                DeprecationWarning,
            )

            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )
            self._ssl_channel_credentials = ssl_credentials
        else:
            host = host if ":" in host else host + ":443"

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_channel_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )

        self._stubs = {}  # type: Dict[str, Callable]

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

    @classmethod
    def create_channel(
        cls,
        host: str = "aiplatform.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optionsl[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if "operations_client" not in self.__dict__:
            self.__dict__["operations_client"] = operations_v1.OperationsClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self.__dict__["operations_client"]

    @property
    def create_endpoint(
        self,
    ) -> Callable[[endpoint_service.CreateEndpointRequest], operations.Operation]:
        r"""Return a callable for the create endpoint method over gRPC.

        Creates an Endpoint.

        Returns:
            Callable[[~.CreateEndpointRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_endpoint" not in self._stubs:
            self._stubs["create_endpoint"] = self.grpc_channel.unary_unary(
                "/google.cloud.aiplatform.v1beta1.EndpointService/CreateEndpoint",
                request_serializer=endpoint_service.CreateEndpointRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["create_endpoint"]

    @property
    def get_endpoint(
        self,
    ) -> Callable[[endpoint_service.GetEndpointRequest], endpoint.Endpoint]:
        r"""Return a callable for the get endpoint method over gRPC.

        Gets an Endpoint.

        Returns:
            Callable[[~.GetEndpointRequest],
                    ~.Endpoint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_endpoint" not in self._stubs:
            self._stubs["get_endpoint"] = self.grpc_channel.unary_unary(
                "/google.cloud.aiplatform.v1beta1.EndpointService/GetEndpoint",
                request_serializer=endpoint_service.GetEndpointRequest.serialize,
                response_deserializer=endpoint.Endpoint.deserialize,
            )
        return self._stubs["get_endpoint"]

    @property
    def list_endpoints(
        self,
    ) -> Callable[
        [endpoint_service.ListEndpointsRequest], endpoint_service.ListEndpointsResponse
    ]:
        r"""Return a callable for the list endpoints method over gRPC.

        Lists Endpoints in a Location.

        Returns:
            Callable[[~.ListEndpointsRequest],
                    ~.ListEndpointsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_endpoints" not in self._stubs:
            self._stubs["list_endpoints"] = self.grpc_channel.unary_unary(
                "/google.cloud.aiplatform.v1beta1.EndpointService/ListEndpoints",
                request_serializer=endpoint_service.ListEndpointsRequest.serialize,
                response_deserializer=endpoint_service.ListEndpointsResponse.deserialize,
            )
        return self._stubs["list_endpoints"]

    @property
    def update_endpoint(
        self,
    ) -> Callable[[endpoint_service.UpdateEndpointRequest], gca_endpoint.Endpoint]:
        r"""Return a callable for the update endpoint method over gRPC.

        Updates an Endpoint.

        Returns:
            Callable[[~.UpdateEndpointRequest],
                    ~.Endpoint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_endpoint" not in self._stubs:
            self._stubs["update_endpoint"] = self.grpc_channel.unary_unary(
                "/google.cloud.aiplatform.v1beta1.EndpointService/UpdateEndpoint",
                request_serializer=endpoint_service.UpdateEndpointRequest.serialize,
                response_deserializer=gca_endpoint.Endpoint.deserialize,
            )
        return self._stubs["update_endpoint"]

    @property
    def delete_endpoint(
        self,
    ) -> Callable[[endpoint_service.DeleteEndpointRequest], operations.Operation]:
        r"""Return a callable for the delete endpoint method over gRPC.

        Deletes an Endpoint.

        Returns:
            Callable[[~.DeleteEndpointRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_endpoint" not in self._stubs:
            self._stubs["delete_endpoint"] = self.grpc_channel.unary_unary(
                "/google.cloud.aiplatform.v1beta1.EndpointService/DeleteEndpoint",
                request_serializer=endpoint_service.DeleteEndpointRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["delete_endpoint"]

    @property
    def deploy_model(
        self,
    ) -> Callable[[endpoint_service.DeployModelRequest], operations.Operation]:
        r"""Return a callable for the deploy model method over gRPC.

        Deploys a Model into this Endpoint, creating a
        DeployedModel within it.

        Returns:
            Callable[[~.DeployModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deploy_model" not in self._stubs:
            self._stubs["deploy_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.aiplatform.v1beta1.EndpointService/DeployModel",
                request_serializer=endpoint_service.DeployModelRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["deploy_model"]

    @property
    def undeploy_model(
        self,
    ) -> Callable[[endpoint_service.UndeployModelRequest], operations.Operation]:
        r"""Return a callable for the undeploy model method over gRPC.

        Undeploys a Model from an Endpoint, removing a
        DeployedModel from it, and freeing all resources it's
        using.

        Returns:
            Callable[[~.UndeployModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undeploy_model" not in self._stubs:
            self._stubs["undeploy_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.aiplatform.v1beta1.EndpointService/UndeployModel",
                request_serializer=endpoint_service.UndeployModelRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["undeploy_model"]


__all__ = ("EndpointServiceGrpcTransport",)
