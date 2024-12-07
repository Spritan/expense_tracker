"""
This type stub file was generated by pyright.
"""

import sys
import warnings

"""
This type stub file was generated by pyright.
"""
class Python37DeprecationWarning(DeprecationWarning):
    """
    Deprecation warning raised when Python 3.7 runtime is detected.
    Python 3.7 support will be dropped after January 1, 2024.
    """
    ...


if sys.version_info.major == 3 and sys.version_info.minor == 7:
    message = ...