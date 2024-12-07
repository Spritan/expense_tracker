"""
This type stub file was generated by pyright.
"""

import logging
import sys
import warnings
from google.auth import version as google_auth_version
from google.auth._default import default, load_credentials_from_dict, load_credentials_from_file

"""
This type stub file was generated by pyright.
"""
__version__ = ...
__all__ = ["default", "load_credentials_from_file", "load_credentials_from_dict"]
class Python37DeprecationWarning(DeprecationWarning):
    """
    Deprecation warning raised when Python 3.7 runtime is detected.
    Python 3.7 support will be dropped after January 1, 2024.
    """
    ...


if sys.version_info.major == 3 and sys.version_info.minor == 7:
    message = ...