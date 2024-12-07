"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
This type stub file was generated by pyright.
"""
DEFAULT_UNIVERSE = ...
class EmptyUniverseError(ValueError):
    def __init__(self) -> None:
        ...
    


class UniverseMismatchError(ValueError):
    def __init__(self, client_universe, credentials_universe) -> None:
        ...
    


def determine_domain(client_universe_domain: Optional[str], universe_domain_env: Optional[str]) -> str:
    """Return the universe domain used by the client.

    Args:
        client_universe_domain (Optional[str]): The universe domain configured via the client options.
        universe_domain_env (Optional[str]): The universe domain configured via the
        "GOOGLE_CLOUD_UNIVERSE_DOMAIN" environment variable.

    Returns:
        str: The universe domain to be used by the client.

    Raises:
        ValueError: If the universe domain is an empty string.
    """
    ...

def compare_domains(client_universe: str, credentials: Any) -> bool:
    """Returns True iff the universe domains used by the client and credentials match.

    Args:
        client_universe (str): The universe domain configured via the client options.
        credentials Any: The credentials being used in the client.

    Returns:
        bool: True iff client_universe matches the universe in credentials.

    Raises:
        ValueError: when client_universe does not match the universe in credentials.
    """
    ...
