"""
This type stub file was generated by pyright.
"""

import datetime
from typing import Iterable, Optional
from google.generativeai import protos
from google.generativeai.types import caching_types, content_types

"""
This type stub file was generated by pyright.
"""
_USER_ROLE = ...
_MODEL_ROLE = ...
class CachedContent:
    """Cached content resource."""
    def __init__(self, name) -> None:
        """Fetches a `CachedContent` resource.

        Identical to `CachedContent.get`.

        Args:
            name: The resource name referring to the cached content.
        """
        ...
    
    @property
    def name(self) -> str:
        ...
    
    @property
    def model(self) -> str:
        ...
    
    @property
    def display_name(self) -> str:
        ...
    
    @property
    def usage_metadata(self) -> protos.CachedContent.UsageMetadata:
        ...
    
    @property
    def create_time(self) -> datetime.datetime:
        ...
    
    @property
    def update_time(self) -> datetime.datetime:
        ...
    
    @property
    def expire_time(self) -> datetime.datetime:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    @classmethod
    def create(cls, model: str, *, display_name: str | None = ..., system_instruction: Optional[content_types.ContentType] = ..., contents: Optional[content_types.ContentsType] = ..., tools: Optional[content_types.FunctionLibraryType] = ..., tool_config: Optional[content_types.ToolConfigType] = ..., ttl: Optional[caching_types.TTLTypes] = ..., expire_time: Optional[caching_types.ExpireTimeTypes] = ...) -> CachedContent:
        """Creates `CachedContent` resource.

        Args:
            model: The name of the `model` to use for cached content creation.
                   Any `CachedContent` resource can be only used with the
                   `model` it was created for.
            display_name: The user-generated meaningful display name
                          of the cached content. `display_name` must be no
                          more than 128 unicode characters.
            system_instruction: Developer set system instruction.
            contents: Contents to cache.
            tools: A list of `Tools` the model may use to generate response.
            tool_config: Config to apply to all tools.
            ttl: TTL for cached resource (in seconds). Defaults to 1 hour.
                 `ttl` and `expire_time` are exclusive arguments.
            expire_time: Expiration time for cached resource.
                         `ttl` and `expire_time` are exclusive arguments.

        Returns:
            `CachedContent` resource with specified name.
        """
        ...
    
    @classmethod
    def get(cls, name: str) -> CachedContent:
        """Fetches required `CachedContent` resource.

        Args:
            name: The resource name referring to the cached content.

        Returns:
            `CachedContent` resource with specified `name`.
        """
        ...
    
    @classmethod
    def list(cls, page_size: Optional[int] = ...) -> Iterable[CachedContent]:
        """Lists `CachedContent` objects associated with the project.

        Args:
            page_size: The maximum number of permissions to return (per page).
            The service may return fewer `CachedContent` objects.

        Returns:
            A paginated list of `CachedContent` objects.
        """
        ...
    
    def delete(self) -> None:
        """Deletes `CachedContent` resource."""
        ...
    
    def update(self, *, ttl: Optional[caching_types.TTLTypes] = ..., expire_time: Optional[caching_types.ExpireTimeTypes] = ...) -> None:
        """Updates requested `CachedContent` resource.

        Args:
            ttl: TTL for cached resource (in seconds). Defaults to 1 hour.
                 `ttl` and `expire_time` are exclusive arguments.
            expire_time: Expiration time for cached resource.
                         `ttl` and `expire_time` are exclusive arguments.
        """
        ...
    

