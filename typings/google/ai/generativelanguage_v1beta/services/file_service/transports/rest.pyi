"""
This type stub file was generated by pyright.
"""

import dataclasses
from typing import Any, Callable, Dict, Optional, Sequence, Tuple
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.auth.transport.requests import AuthorizedSession
from google.protobuf import empty_pb2
from google.ai.generativelanguage_v1beta.types import file, file_service
from .base import FileServiceTransport

OptionalRetry = ...
DEFAULT_CLIENT_INFO = ...
class FileServiceRestInterceptor:
    """Interceptor for FileService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the FileServiceRestTransport.

    .. code-block:: python
        class MyCustomFileServiceInterceptor(FileServiceRestInterceptor):
            def pre_create_file(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_file(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_file(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_file(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_file(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_files(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_files(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = FileServiceRestTransport(interceptor=MyCustomFileServiceInterceptor())
        client = FileServiceClient(transport=transport)


    """
    def pre_create_file(self, request: file_service.CreateFileRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[file_service.CreateFileRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_file

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FileService server.
        """
        ...
    
    def post_create_file(self, response: file_service.CreateFileResponse) -> file_service.CreateFileResponse:
        """Post-rpc interceptor for create_file

        Override in a subclass to manipulate the response
        after it is returned by the FileService server but before
        it is returned to user code.
        """
        ...
    
    def pre_delete_file(self, request: file_service.DeleteFileRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[file_service.DeleteFileRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_file

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FileService server.
        """
        ...
    
    def pre_get_file(self, request: file_service.GetFileRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[file_service.GetFileRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_file

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FileService server.
        """
        ...
    
    def post_get_file(self, response: file.File) -> file.File:
        """Post-rpc interceptor for get_file

        Override in a subclass to manipulate the response
        after it is returned by the FileService server but before
        it is returned to user code.
        """
        ...
    
    def pre_list_files(self, request: file_service.ListFilesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[file_service.ListFilesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_files

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FileService server.
        """
        ...
    
    def post_list_files(self, response: file_service.ListFilesResponse) -> file_service.ListFilesResponse:
        """Post-rpc interceptor for list_files

        Override in a subclass to manipulate the response
        after it is returned by the FileService server but before
        it is returned to user code.
        """
        ...
    


@dataclasses.dataclass
class FileServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: FileServiceRestInterceptor
    ...


class FileServiceRestTransport(FileServiceTransport):
    """REST backend transport for FileService.

    An API for uploading and managing files.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """
    def __init__(self, *, host: str = ..., credentials: Optional[ga_credentials.Credentials] = ..., credentials_file: Optional[str] = ..., scopes: Optional[Sequence[str]] = ..., client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = ..., quota_project_id: Optional[str] = ..., client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: Optional[bool] = ..., url_scheme: str = ..., interceptor: Optional[FileServiceRestInterceptor] = ..., api_audience: Optional[str] = ...) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'generativelanguage.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        ...
    
    class _CreateFile(FileServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        def __call__(self, request: file_service.CreateFileRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> file_service.CreateFileResponse:
            r"""Call the create file method over HTTP.

            Args:
                request (~.file_service.CreateFileRequest):
                    The request object. Request for ``CreateFile``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.file_service.CreateFileResponse:
                    Response for ``CreateFile``.
            """
            ...
        
    
    
    class _DeleteFile(FileServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: file_service.DeleteFileRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...): # -> None:
            r"""Call the delete file method over HTTP.

            Args:
                request (~.file_service.DeleteFileRequest):
                    The request object. Request for ``DeleteFile``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """
            ...
        
    
    
    class _GetFile(FileServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: file_service.GetFileRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> file.File:
            r"""Call the get file method over HTTP.

            Args:
                request (~.file_service.GetFileRequest):
                    The request object. Request for ``GetFile``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.file.File:
                    A file uploaded to the API.
            """
            ...
        
    
    
    class _ListFiles(FileServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        def __call__(self, request: file_service.ListFilesRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> file_service.ListFilesResponse:
            r"""Call the list files method over HTTP.

            Args:
                request (~.file_service.ListFilesRequest):
                    The request object. Request for ``ListFiles``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.file_service.ListFilesResponse:
                    Response for ``ListFiles``.
            """
            ...
        
    
    
    @property
    def create_file(self) -> Callable[[file_service.CreateFileRequest], file_service.CreateFileResponse]:
        ...
    
    @property
    def delete_file(self) -> Callable[[file_service.DeleteFileRequest], empty_pb2.Empty]:
        ...
    
    @property
    def get_file(self) -> Callable[[file_service.GetFileRequest], file.File]:
        ...
    
    @property
    def list_files(self) -> Callable[[file_service.ListFilesRequest], file_service.ListFilesResponse]:
        ...
    
    @property
    def kind(self) -> str:
        ...
    
    def close(self): # -> None:
        ...
    


__all__ = ("FileServiceRestTransport", )
