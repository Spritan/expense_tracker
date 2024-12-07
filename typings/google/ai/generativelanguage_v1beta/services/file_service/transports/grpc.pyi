"""
This type stub file was generated by pyright.
"""

import grpc
from typing import Callable, Dict, Optional, Sequence, Tuple, Union
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.protobuf import empty_pb2
from google.ai.generativelanguage_v1beta.types import file, file_service
from .base import FileServiceTransport

class FileServiceGrpcTransport(FileServiceTransport):
    """gRPC backend transport for FileService.

    An API for uploading and managing files.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]
    def __init__(self, *, host: str = ..., credentials: Optional[ga_credentials.Credentials] = ..., credentials_file: Optional[str] = ..., scopes: Optional[Sequence[str]] = ..., channel: Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]] = ..., api_mtls_endpoint: Optional[str] = ..., client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = ..., ssl_channel_credentials: Optional[grpc.ChannelCredentials] = ..., client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = ..., quota_project_id: Optional[str] = ..., client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: Optional[bool] = ..., api_audience: Optional[str] = ...) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'generativelanguage.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if a ``channel`` instance is provided.
            channel (Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]]):
                A ``Channel`` instance through which to make calls, or a Callable
                that constructs and returns one. If set to None, ``self.create_channel``
                is used to create the channel. If a Callable is given, it will be called
                with the same arguments as used in ``self.create_channel``.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if a ``channel`` instance is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if a ``channel`` instance or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        ...
    
    @classmethod
    def create_channel(cls, host: str = ..., credentials: Optional[ga_credentials.Credentials] = ..., credentials_file: Optional[str] = ..., scopes: Optional[Sequence[str]] = ..., quota_project_id: Optional[str] = ..., **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
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
        ...
    
    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        ...
    
    @property
    def create_file(self) -> Callable[[file_service.CreateFileRequest], file_service.CreateFileResponse]:
        r"""Return a callable for the create file method over gRPC.

        Creates a ``File``.

        Returns:
            Callable[[~.CreateFileRequest],
                    ~.CreateFileResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    @property
    def list_files(self) -> Callable[[file_service.ListFilesRequest], file_service.ListFilesResponse]:
        r"""Return a callable for the list files method over gRPC.

        Lists the metadata for ``File``\ s owned by the requesting
        project.

        Returns:
            Callable[[~.ListFilesRequest],
                    ~.ListFilesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    @property
    def get_file(self) -> Callable[[file_service.GetFileRequest], file.File]:
        r"""Return a callable for the get file method over gRPC.

        Gets the metadata for the given ``File``.

        Returns:
            Callable[[~.GetFileRequest],
                    ~.File]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    @property
    def delete_file(self) -> Callable[[file_service.DeleteFileRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete file method over gRPC.

        Deletes the ``File``.

        Returns:
            Callable[[~.DeleteFileRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    def close(self): # -> None:
        ...
    
    @property
    def kind(self) -> str:
        ...
    


__all__ = ("FileServiceGrpcTransport", )
