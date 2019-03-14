from rest_framework import permissions

SAFE_METHODS = ['GET', 'PUT', 'HEAD', 'OPTIONS']

class IsUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj == request.user
