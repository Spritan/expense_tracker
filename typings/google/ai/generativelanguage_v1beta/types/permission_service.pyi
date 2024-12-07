"""
This type stub file was generated by pyright.
"""

import proto
from typing import MutableSequence
from google.protobuf import field_mask_pb2
from google.ai.generativelanguage_v1beta.types import permission as gag_permission

"""
This type stub file was generated by pyright.
"""
__protobuf__ = ...
class CreatePermissionRequest(proto.Message):
    r"""Request to create a ``Permission``.

    Attributes:
        parent (str):
            Required. The parent resource of the ``Permission``.
            Formats: ``tunedModels/{tuned_model}`` ``corpora/{corpus}``
        permission (google.ai.generativelanguage_v1beta.types.Permission):
            Required. The permission to create.
    """
    parent: str = ...
    permission: gag_permission.Permission = ...


class GetPermissionRequest(proto.Message):
    r"""Request for getting information about a specific ``Permission``.

    Attributes:
        name (str):
            Required. The resource name of the permission.

            Formats:
            ``tunedModels/{tuned_model}/permissions/{permission}``
            ``corpora/{corpus}/permissions/{permission}``
    """
    name: str = ...


class ListPermissionsRequest(proto.Message):
    r"""Request for listing permissions.

    Attributes:
        parent (str):
            Required. The parent resource of the permissions. Formats:
            ``tunedModels/{tuned_model}`` ``corpora/{corpus}``
        page_size (int):
            Optional. The maximum number of ``Permission``\ s to return
            (per page). The service may return fewer permissions.

            If unspecified, at most 10 permissions will be returned.
            This method returns at most 1000 permissions per page, even
            if you pass larger page_size.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListPermissions`` call.

            Provide the ``page_token`` returned by one request as an
            argument to the next request to retrieve the next page.

            When paginating, all other parameters provided to
            ``ListPermissions`` must match the call that provided the
            page token.
    """
    parent: str = ...
    page_size: int = ...
    page_token: str = ...


class ListPermissionsResponse(proto.Message):
    r"""Response from ``ListPermissions`` containing a paginated list of
    permissions.

    Attributes:
        permissions (MutableSequence[google.ai.generativelanguage_v1beta.types.Permission]):
            Returned permissions.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page.

            If this field is omitted, there are no more pages.
    """
    @property
    def raw_page(self):
        ...
    
    permissions: MutableSequence[gag_permission.Permission] = ...
    next_page_token: str = ...


class UpdatePermissionRequest(proto.Message):
    r"""Request to update the ``Permission``.

    Attributes:
        permission (google.ai.generativelanguage_v1beta.types.Permission):
            Required. The permission to update.

            The permission's ``name`` field is used to identify the
            permission to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. Accepted ones:

            -  role (``Permission.role`` field)
    """
    permission: gag_permission.Permission = ...
    update_mask: field_mask_pb2.FieldMask = ...


class DeletePermissionRequest(proto.Message):
    r"""Request to delete the ``Permission``.

    Attributes:
        name (str):
            Required. The resource name of the permission. Formats:
            ``tunedModels/{tuned_model}/permissions/{permission}``
            ``corpora/{corpus}/permissions/{permission}``
    """
    name: str = ...


class TransferOwnershipRequest(proto.Message):
    r"""Request to transfer the ownership of the tuned model.

    Attributes:
        name (str):
            Required. The resource name of the tuned model to transfer
            ownership.

            Format: ``tunedModels/my-model-id``
        email_address (str):
            Required. The email address of the user to
            whom the tuned model is being transferred to.
    """
    name: str = ...
    email_address: str = ...


class TransferOwnershipResponse(proto.Message):
    r"""Response from ``TransferOwnership``."""
    ...


__all__ = tuple(sorted(__protobuf__.manifest))
