from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        SAFE_METHODS = ['GET', 'PUT', 'PATCH', 'DELETE']
        if request.method in SAFE_METHODS:
            return True
        return obj.created_by == request.user
