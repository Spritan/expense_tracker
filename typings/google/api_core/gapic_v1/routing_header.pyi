"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
ROUTING_METADATA_KEY = ...
ROUTING_PARAM_CACHE_SIZE = ...
def to_routing_header(params, qualified_enums=...):
    """Returns a routing header string for the given request parameters.

    Args:
        params (Mapping[str, str | bytes | Enum]): A dictionary containing the request
            parameters used for routing.
        qualified_enums (bool): Whether to represent enum values
            as their type-qualified symbol names instead of as their
            unqualified symbol names.

    Returns:
        str: The routing header string.
    """
    ...

def to_grpc_metadata(params, qualified_enums=...):
    """Returns the gRPC metadata containing the routing headers for the given
    request parameters.

    Args:
        params (Mapping[str, str | bytes | Enum]): A dictionary containing the request
            parameters used for routing.
        qualified_enums (bool): Whether to represent enum values
            as their type-qualified symbol names instead of as their
            unqualified symbol names.

    Returns:
        Tuple(str, str): The gRPC metadata containing the routing header key
            and value.
    """
    ...

