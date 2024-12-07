"""
This type stub file was generated by pyright.
"""

import datetime
from typing import Union
from typing_extensions import TypedDict

"""
This type stub file was generated by pyright.
"""
__all__ = ["ExpireTime", "TTL", "TTLTypes", "ExpireTimeTypes"]
class TTL(TypedDict):
    seconds: int
    nanos: int
    ...


class ExpireTime(TypedDict):
    seconds: int
    nanos: int
    ...


TTLTypes = Union[TTL, int, datetime.timedelta]
ExpireTimeTypes = Union[ExpireTime, int, datetime.datetime]
def to_optional_ttl(ttl: TTLTypes | None) -> TTL | None:
    ...

def to_optional_expire_time(expire_time: ExpireTimeTypes | None) -> ExpireTime | None:
    ...

