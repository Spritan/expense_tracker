"""
This type stub file was generated by pyright.
"""

import abc
from typing import Awaitable, Callable, Optional, Sequence, Union
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.ai.generativelanguage_v1beta.types import prediction_service

"""
This type stub file was generated by pyright.
"""
DEFAULT_CLIENT_INFO = ...
class PredictionServiceTransport(abc.ABC):
    """Abstract transport class for PredictionService."""
    AUTH_SCOPES = ...
    DEFAULT_HOST: str = ...
    def __init__(self, *, host: str = ..., credentials: Optional[ga_credentials.Credentials] = ..., credentials_file: Optional[str] = ..., scopes: Optional[Sequence[str]] = ..., quota_project_id: Optional[str] = ..., client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: Optional[bool] = ..., api_audience: Optional[str] = ..., **kwargs) -> None:
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
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """
        ...
    
    @property
    def host(self):
        ...
    
    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        ...
    
    @property
    def predict(self) -> Callable[[prediction_service.PredictRequest], Union[prediction_service.PredictResponse, Awaitable[prediction_service.PredictResponse],],]:
        ...
    
    @property
    def kind(self) -> str:
        ...
    


__all__ = ("PredictionServiceTransport", )