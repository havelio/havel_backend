from rest_framework import status
from rest_framework.permissions import BasePermission

from .exceptions import APIError


class IsSecure(BasePermission):
    """
    Allows access only to secured request (HTTPS).
    """
    def has_permission(self, request, view):
        if not request.is_secure():
            raise APIError(status_code=status.HTTP_403_FORBIDDEN,
                           detail="HTTPS connection is required")
        return True
