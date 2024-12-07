"""
This type stub file was generated by pyright.
"""

import dataclasses
from typing import Any, Callable, Dict, Optional, Sequence, Tuple
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.auth.transport.requests import AuthorizedSession
from google.protobuf import empty_pb2
from google.longrunning import operations_pb2
from google.ai.generativelanguage_v1beta.types import model, model_service, tuned_model as gag_tuned_model
from .base import ModelServiceTransport

OptionalRetry = ...
DEFAULT_CLIENT_INFO = ...
class ModelServiceRestInterceptor:
    """Interceptor for ModelService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ModelServiceRestTransport.

    .. code-block:: python
        class MyCustomModelServiceInterceptor(ModelServiceRestInterceptor):
            def pre_create_tuned_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tuned_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tuned_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tuned_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tuned_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_models(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_models(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tuned_models(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tuned_models(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tuned_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tuned_model(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ModelServiceRestTransport(interceptor=MyCustomModelServiceInterceptor())
        client = ModelServiceClient(transport=transport)


    """
    def pre_create_tuned_model(self, request: model_service.CreateTunedModelRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[model_service.CreateTunedModelRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_tuned_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        """
        ...
    
    def post_create_tuned_model(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_tuned_model

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        """
        ...
    
    def pre_delete_tuned_model(self, request: model_service.DeleteTunedModelRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[model_service.DeleteTunedModelRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_tuned_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        """
        ...
    
    def pre_get_model(self, request: model_service.GetModelRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[model_service.GetModelRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        """
        ...
    
    def post_get_model(self, response: model.Model) -> model.Model:
        """Post-rpc interceptor for get_model

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        """
        ...
    
    def pre_get_tuned_model(self, request: model_service.GetTunedModelRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[model_service.GetTunedModelRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_tuned_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        """
        ...
    
    def post_get_tuned_model(self, response: tuned_model.TunedModel) -> tuned_model.TunedModel:
        """Post-rpc interceptor for get_tuned_model

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        """
        ...
    
    def pre_list_models(self, request: model_service.ListModelsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[model_service.ListModelsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_models

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        """
        ...
    
    def post_list_models(self, response: model_service.ListModelsResponse) -> model_service.ListModelsResponse:
        """Post-rpc interceptor for list_models

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        """
        ...
    
    def pre_list_tuned_models(self, request: model_service.ListTunedModelsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[model_service.ListTunedModelsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_tuned_models

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        """
        ...
    
    def post_list_tuned_models(self, response: model_service.ListTunedModelsResponse) -> model_service.ListTunedModelsResponse:
        """Post-rpc interceptor for list_tuned_models

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        """
        ...
    
    def pre_update_tuned_model(self, request: model_service.UpdateTunedModelRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[model_service.UpdateTunedModelRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_tuned_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        """
        ...
    
    def post_update_tuned_model(self, response: gag_tuned_model.TunedModel) -> gag_tuned_model.TunedModel:
        """Post-rpc interceptor for update_tuned_model

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        """
        ...
    


@dataclasses.dataclass
class ModelServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ModelServiceRestInterceptor
    ...


class ModelServiceRestTransport(ModelServiceTransport):
    """REST backend transport for ModelService.

    Provides methods for getting metadata information about
    Generative Models.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """
    def __init__(self, *, host: str = ..., credentials: Optional[ga_credentials.Credentials] = ..., credentials_file: Optional[str] = ..., scopes: Optional[Sequence[str]] = ..., client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = ..., quota_project_id: Optional[str] = ..., client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: Optional[bool] = ..., url_scheme: str = ..., interceptor: Optional[ModelServiceRestInterceptor] = ..., api_audience: Optional[str] = ...) -> None:
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
    
    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        ...
    
    class _CreateTunedModel(ModelServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: model_service.CreateTunedModelRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> operations_pb2.Operation:
            r"""Call the create tuned model method over HTTP.

            Args:
                request (~.model_service.CreateTunedModelRequest):
                    The request object. Request to create a TunedModel.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """
            ...
        
    
    
    class _DeleteTunedModel(ModelServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: model_service.DeleteTunedModelRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...): # -> None:
            r"""Call the delete tuned model method over HTTP.

            Args:
                request (~.model_service.DeleteTunedModelRequest):
                    The request object. Request to delete a TunedModel.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """
            ...
        
    
    
    class _GetModel(ModelServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: model_service.GetModelRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> model.Model:
            r"""Call the get model method over HTTP.

            Args:
                request (~.model_service.GetModelRequest):
                    The request object. Request for getting information about
                a specific Model.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.model.Model:
                    Information about a Generative
                Language Model.

            """
            ...
        
    
    
    class _GetTunedModel(ModelServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: model_service.GetTunedModelRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> tuned_model.TunedModel:
            r"""Call the get tuned model method over HTTP.

            Args:
                request (~.model_service.GetTunedModelRequest):
                    The request object. Request for getting information about
                a specific Model.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.tuned_model.TunedModel:
                    A fine-tuned model created using
                ModelService.CreateTunedModel.

            """
            ...
        
    
    
    class _ListModels(ModelServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        def __call__(self, request: model_service.ListModelsRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> model_service.ListModelsResponse:
            r"""Call the list models method over HTTP.

            Args:
                request (~.model_service.ListModelsRequest):
                    The request object. Request for listing all Models.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.model_service.ListModelsResponse:
                    Response from ``ListModel`` containing a paginated list
                of Models.

            """
            ...
        
    
    
    class _ListTunedModels(ModelServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        def __call__(self, request: model_service.ListTunedModelsRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> model_service.ListTunedModelsResponse:
            r"""Call the list tuned models method over HTTP.

            Args:
                request (~.model_service.ListTunedModelsRequest):
                    The request object. Request for listing TunedModels.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.model_service.ListTunedModelsResponse:
                    Response from ``ListTunedModels`` containing a paginated
                list of Models.

            """
            ...
        
    
    
    class _UpdateTunedModel(ModelServiceRestStub):
        def __hash__(self) -> int:
            ...
        
        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = ...
        def __call__(self, request: model_service.UpdateTunedModelRequest, *, retry: OptionalRetry = ..., timeout: Optional[float] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> gag_tuned_model.TunedModel:
            r"""Call the update tuned model method over HTTP.

            Args:
                request (~.model_service.UpdateTunedModelRequest):
                    The request object. Request to update a TunedModel.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gag_tuned_model.TunedModel:
                    A fine-tuned model created using
                ModelService.CreateTunedModel.

            """
            ...
        
    
    
    @property
    def create_tuned_model(self) -> Callable[[model_service.CreateTunedModelRequest], operations_pb2.Operation]:
        ...
    
    @property
    def delete_tuned_model(self) -> Callable[[model_service.DeleteTunedModelRequest], empty_pb2.Empty]:
        ...
    
    @property
    def get_model(self) -> Callable[[model_service.GetModelRequest], model.Model]:
        ...
    
    @property
    def get_tuned_model(self) -> Callable[[model_service.GetTunedModelRequest], tuned_model.TunedModel]:
        ...
    
    @property
    def list_models(self) -> Callable[[model_service.ListModelsRequest], model_service.ListModelsResponse]:
        ...
    
    @property
    def list_tuned_models(self) -> Callable[[model_service.ListTunedModelsRequest], model_service.ListTunedModelsResponse]:
        ...
    
    @property
    def update_tuned_model(self) -> Callable[[model_service.UpdateTunedModelRequest], gag_tuned_model.TunedModel]:
        ...
    
    @property
    def kind(self) -> str:
        ...
    
    def close(self): # -> None:
        ...
    


__all__ = ("ModelServiceRestTransport", )