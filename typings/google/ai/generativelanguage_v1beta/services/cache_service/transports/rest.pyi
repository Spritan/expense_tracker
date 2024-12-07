"""
This type stub file was generated by pyright.
"""

import dataclasses
from typing import Any, Callable, Dict, Optional, Sequence, Tuple
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.auth.transport.requests import AuthorizedSession
from google.protobuf import empty_pb2
from google.ai.generativelanguage_v1beta.types import cache_service, cached_content as gag_cached_content
from .base import CacheServiceTransport

OptionalRetry = ...
DEFAULT_CLIENT_INFO = ...
class CacheServiceRestInterceptor:
    """Interceptor for CacheService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CacheServiceRestTransport.

    .. code-block:: python
        class MyCustomCacheServiceInterceptor(CacheServiceRestInterceptor):
            def pre_create_cached_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_cached_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_cached_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_cached_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_cached_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_cached_contents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_cached_contents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_cached_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_cached_content(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CacheServiceRestTransport(interceptor=MyCustomCacheServiceInterceptor())
        client = CacheServiceClient(transport=transport)


    """
    def pre_create_cached_content(self, request: cache_service.CreateCachedContentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cache_service.CreateCachedContentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_cached_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CacheService server.
        """
        ...
    
    def post_create_cached_content(self, response: gag_cached_content.CachedContent) -> gag_cached_content.CachedContent:
        """Post-rpc interceptor for create_cached_content

        Override in a subclass to manipulate the response
        after it is returned by the CacheService server but before
        it is returned to user code.
        """
        ...
    
    def pre_delete_cached_content(self, request: cache_service.DeleteCachedContentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cache_service.DeleteCachedContentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_cached_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CacheService server.
        """
        ...
    
    def pre_get_cached_content(self, request: cache_service.GetCachedContentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cache_service.GetCachedContentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_cached_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CacheService server.
        """
        ...
    
    def post_get_cached_content(self, response: cached_content.CachedContent) -> cached_content.CachedContent:
        """Post-rpc interceptor for get_cached_content

        Override in a subclass to manipulate the response
        after it is returned by the CacheService server but before
        it is returned to user code.
        """
        ...
    
    def pre_list_cached_contents(self, request: cache_service.ListCachedContentsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cache_service.ListCachedContentsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_cached_contents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CacheService server.
        """
        ...
    
    def post_list_cached_contents(self, response: cache_service.ListCachedContentsResponse) -> cache_service.ListCachedContentsResponse:
        """Post-rpc interceptor for list_cached_contents

        Override in a subclass to manipulate the response
        after it is returned by the CacheService server but before
        it is returned to user code.
        """
        ...
    
    def pre_update_cached_content(self, request: cache_service.UpdateCachedContentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cache_service.UpdateCachedContentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_cached_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CacheService server.
        """
        ...
    
    def post_update_cached_content(self, response: gag_cached_content.CachedContent) -> gag_cached_content.CachedContent:
        """Post-rpc interceptor for update_cached_content

        Override in a subclass to manipulate the response
        after it is returned by the CacheService server but before
        it is returned to user code.
        """
        ...
    


@dataclasses.dataclass
class CacheServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CacheServiceRestInterceptor
    ...


class CacheServiceRestTransport(CacheServiceTransport):
    """REST backend transport for CacheService.

    API for managing cache of content (CachedContent resources)
    that can be used in GenerativeService requests. This way
    generate content requests can benefit from preprocessing work
    being done earlier, possibly lowering their computational cost.
    It is intended to be used with large contexts.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """
    def __init__(self, *, host: str = ..., credentials: Optional[ga_credentials.Credentials] = ..., credentials_file: Optional[str] = ..., scopes: Optional[Sequence[str]] = ..., client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = ..., quota_project_id: Optional[str] = ..., client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: Optional[bool] = ..., url_scheme: str = ..., interceptor: Optional[CacheServiceRestInterceptor] = ..., api_audience: Optional[str] = ...) -> None:
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
    
    class _CreateCachedContent(CacheServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: cache_service.CreateCachedContentRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> gag_cached_content.CachedContent:
            r"""Call the create cached content method over HTTP.

            Args:
                request (~.cache_service.CreateCachedContentRequest):
                    The request object. Request to create CachedContent.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gag_cached_content.CachedContent:
                    Content that has been preprocessed
                and can be used in subsequent request to
                GenerativeService.

                Cached content can be only used with
                model it was created for.

            """
            ...
        
    
    
    class _DeleteCachedContent(CacheServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: cache_service.DeleteCachedContentRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...): # -> None:
            r"""Call the delete cached content method over HTTP.

            Args:
                request (~.cache_service.DeleteCachedContentRequest):
                    The request object. Request to delete CachedContent.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """
            ...
        
    
    
    class _GetCachedContent(CacheServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: cache_service.GetCachedContentRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> cached_content.CachedContent:
            r"""Call the get cached content method over HTTP.

            Args:
                request (~.cache_service.GetCachedContentRequest):
                    The request object. Request to read CachedContent.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.cached_content.CachedContent:
                    Content that has been preprocessed
                and can be used in subsequent request to
                GenerativeService.

                Cached content can be only used with
                model it was created for.

            """
            ...
        
    
    
    class _ListCachedContents(CacheServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        def __call__(self, request: cache_service.ListCachedContentsRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> cache_service.ListCachedContentsResponse:
            r"""Call the list cached contents method over HTTP.

            Args:
                request (~.cache_service.ListCachedContentsRequest):
                    The request object. Request to list CachedContents.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.cache_service.ListCachedContentsResponse:
                    Response with CachedContents list.
            """
            ...
        
    
    
    class _UpdateCachedContent(CacheServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: cache_service.UpdateCachedContentRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> gag_cached_content.CachedContent:
            r"""Call the update cached content method over HTTP.

            Args:
                request (~.cache_service.UpdateCachedContentRequest):
                    The request object. Request to update CachedContent.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gag_cached_content.CachedContent:
                    Content that has been preprocessed
                and can be used in subsequent request to
                GenerativeService.

                Cached content can be only used with
                model it was created for.

            """
            ...
        
    
    
    @property
    def create_cached_content(self) -> Callable[[cache_service.CreateCachedContentRequest], gag_cached_content.CachedContent]:
        ...
    
    @property
    def delete_cached_content(self) -> Callable[[cache_service.DeleteCachedContentRequest], empty_pb2.Empty]:
        ...
    
    @property
    def get_cached_content(self) -> Callable[[cache_service.GetCachedContentRequest], cached_content.CachedContent]:
        ...
    
    @property
    def list_cached_contents(self) -> Callable[[cache_service.ListCachedContentsRequest], cache_service.ListCachedContentsResponse,]:
        ...
    
    @property
    def update_cached_content(self) -> Callable[[cache_service.UpdateCachedContentRequest], gag_cached_content.CachedContent]:
        ...
    
    @property
    def kind(self) -> str:
        ...
    
    def close(self): # -> None:
        ...
    


__all__ = ("CacheServiceRestTransport", )
