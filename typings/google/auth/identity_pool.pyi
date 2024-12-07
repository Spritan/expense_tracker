"""
This type stub file was generated by pyright.
"""

import abc
from typing import NamedTuple
from google.auth import _helpers, external_account

"""Identity Pool Credentials.

This module provides credentials to access Google Cloud resources from on-prem
or non-Google Cloud platforms which support external credentials (e.g. OIDC ID
tokens) retrieved from local file locations or local servers. This includes
Microsoft Azure and OIDC identity providers (e.g. K8s workloads registered with
Hub with Hub workload identity enabled).

These credentials are recommended over the use of service account credentials
in on-prem/non-Google Cloud platforms as they do not involve the management of
long-live service account private keys.

Identity Pool Credentials are initialized using external_account
arguments which are typically loaded from an external credentials file or
an external credentials URL.

This module also provides a definition for an abstract subject token supplier.
This supplier can be implemented to return a valid OIDC or SAML2.0 subject token
and used to create Identity Pool credentials. The credentials will then call the
supplier instead of using pre-defined methods such as reading a local file or
calling a URL.
"""
class SubjectTokenSupplier(metaclass=abc.ABCMeta):
    """Base class for subject token suppliers. This can be implemented with custom logic to retrieve
    a subject token to exchange for a Google Cloud access token when using Workload or
    Workforce Identity Federation. The identity pool credential does not cache the subject token,
    so caching logic should be added in the implementation.
    """
    @abc.abstractmethod
    def get_subject_token(self, context, request):
        """Returns the requested subject token. The subject token must be valid.

        .. warning: This is not cached by the calling Google credential, so caching logic should be implemented in the supplier.

        Args:
            context (google.auth.externalaccount.SupplierContext): The context object
                containing information about the requested audience and subject token type.
            request (google.auth.transport.Request): The object used to make
                HTTP requests.

        Raises:
            google.auth.exceptions.RefreshError: If an error is encountered during
                subject token retrieval logic.

        Returns:
            str: The requested subject token string.
        """
        ...
    


class _TokenContent(NamedTuple):
    """Models the token content response from file and url internal suppliers.
        Attributes:
            content (str): The string content of the file or URL response.
            location (str): The location the content was retrieved from. This will either be a file location or a URL.
    """
    content: str
    location: str
    ...


class _FileSupplier(SubjectTokenSupplier):
    """ Internal implementation of subject token supplier which supports reading a subject token from a file."""
    def __init__(self, path, format_type, subject_token_field_name) -> None:
        ...
    
    @_helpers.copy_docstring(SubjectTokenSupplier)
    def get_subject_token(self, context, request): # -> Any:
        ...
    


class _UrlSupplier(SubjectTokenSupplier):
    """ Internal implementation of subject token supplier which supports retrieving a subject token by calling a URL endpoint."""
    def __init__(self, url, format_type, subject_token_field_name, headers) -> None:
        ...
    
    @_helpers.copy_docstring(SubjectTokenSupplier)
    def get_subject_token(self, context, request): # -> Any:
        ...
    


class _X509Supplier(SubjectTokenSupplier):
    """Internal supplier for X509 workload credentials. This class is used internally and always returns an empty string as the subject token."""
    @_helpers.copy_docstring(SubjectTokenSupplier)
    def get_subject_token(self, context, request): # -> Literal['']:
        ...
    


class Credentials(external_account.Credentials):
    """External account credentials sourced from files and URLs."""
    def __init__(self, audience, subject_token_type, token_url=..., credential_source=..., subject_token_supplier=..., *args, **kwargs) -> None:
        """Instantiates an external account credentials object from a file/URL.

        Args:
            audience (str): The STS audience field.
            subject_token_type (str): The subject token type based on the Oauth2.0 token exchange spec.
                Expected values include::

                    “urn:ietf:params:oauth:token-type:jwt”
                    “urn:ietf:params:oauth:token-type:id-token”
                    “urn:ietf:params:oauth:token-type:saml2”

            token_url (Optional [str]): The STS endpoint URL. If not provided, will default to "https://sts.googleapis.com/v1/token".
            credential_source (Optional [Mapping]): The credential source dictionary used to
                provide instructions on how to retrieve external credential to be
                exchanged for Google access tokens. Either a credential source or
                a subject token supplier must be provided.

                Example credential_source for url-sourced credential::

                    {
                        "url": "http://www.example.com",
                        "format": {
                            "type": "json",
                            "subject_token_field_name": "access_token",
                        },
                        "headers": {"foo": "bar"},
                    }

                Example credential_source for file-sourced credential::

                    {
                        "file": "/path/to/token/file.txt"
                    }
            subject_token_supplier (Optional [SubjectTokenSupplier]): Optional subject token supplier.
                This will be called to supply a valid subject token which will then
                be exchanged for Google access tokens. Either a subject token  supplier
                or a credential source must be provided.
            args (List): Optional positional arguments passed into the underlying :meth:`~external_account.Credentials.__init__` method.
            kwargs (Mapping): Optional keyword arguments passed into the underlying :meth:`~external_account.Credentials.__init__` method.

        Raises:
            google.auth.exceptions.RefreshError: If an error is encountered during
                access token retrieval logic.
            ValueError: For invalid parameters.

        .. note:: Typically one of the helper constructors
            :meth:`from_file` or
            :meth:`from_info` are used instead of calling the constructor directly.
        """
        ...
    
    @_helpers.copy_docstring(external_account.Credentials)
    def retrieve_subject_token(self, request): # -> Any | Literal['']:
        ...
    
    @classmethod
    def from_info(cls, info, **kwargs): # -> Self:
        """Creates an Identity Pool Credentials instance from parsed external account info.

        Args:
            info (Mapping[str, str]): The Identity Pool external account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.identity_pool.Credentials: The constructed
                credentials.

        Raises:
            ValueError: For invalid parameters.
        """
        ...
    
    @classmethod
    def from_file(cls, filename, **kwargs): # -> Self:
        """Creates an IdentityPool Credentials instance from an external account json file.

        Args:
            filename (str): The path to the IdentityPool external account json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.identity_pool.Credentials: The constructed
                credentials.
        """
        ...
    


