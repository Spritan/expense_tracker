"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass(frozen=True)
class PublicKeyCredentialDescriptor:
    """Descriptor for a security key based credential.

    https://www.w3.org/TR/webauthn-3/#dictionary-credential-descriptor

    Args:
        id: <url-safe base64-encoded> credential id (key handle).
        transports: <'usb'|'nfc'|'ble'|'internal'> List of supported transports.
    """
    id: str
    transports: Optional[List[str]] = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    


@dataclass
class AuthenticationExtensionsClientInputs:
    """Client extensions inputs for WebAuthn extensions.

    Args:
        appid: app id that can be asserted with in addition to rpid.
            https://www.w3.org/TR/webauthn-3/#sctn-appid-extension
    """
    appid: Optional[str] = ...
    def to_dict(self): # -> dict[Any, Any]:
        ...
    


@dataclass
class GetRequest:
    """WebAuthn get request

    Args:
        origin: Origin where the WebAuthn get assertion takes place.
        rpid: Relying Party ID.
        challenge: <url-safe base64-encoded> raw challenge.
        timeout_ms: Timeout number in millisecond.
        allow_credentials: List of allowed credentials.
        user_verification: <'required'|'preferred'|'discouraged'> User verification requirement.
        extensions: WebAuthn authentication extensions inputs.
    """
    origin: str
    rpid: str
    challenge: str
    timeout_ms: Optional[int] = ...
    allow_credentials: Optional[List[PublicKeyCredentialDescriptor]] = ...
    user_verification: Optional[str] = ...
    extensions: Optional[AuthenticationExtensionsClientInputs] = ...
    def to_json(self) -> str:
        ...
    


@dataclass(frozen=True)
class AuthenticatorAssertionResponse:
    """Authenticator response to a WebAuthn get (assertion) request.

    https://www.w3.org/TR/webauthn-3/#authenticatorassertionresponse

    Args:
        client_data_json: <url-safe base64-encoded> client data JSON.
        authenticator_data: <url-safe base64-encoded> authenticator data.
        signature: <url-safe base64-encoded> signature.
        user_handle: <url-safe base64-encoded> user handle.
    """
    client_data_json: str
    authenticator_data: str
    signature: str
    user_handle: Optional[str]
    ...


@dataclass(frozen=True)
class GetResponse:
    """WebAuthn get (assertion) response.

    Args:
        id: <url-safe base64-encoded> credential id (key handle).
        response: The authenticator assertion response.
        authenticator_attachment: <'cross-platform'|'platform'> The attachment status of the authenticator.
        client_extension_results: WebAuthn authentication extensions output results in a dictionary.
    """
    id: str
    response: AuthenticatorAssertionResponse
    authenticator_attachment: Optional[str]
    client_extension_results: Optional[Dict]
    @staticmethod
    def from_json(json_str: str): # -> GetResponse:
        """Verify and construct GetResponse from a JSON string."""
        ...
    


