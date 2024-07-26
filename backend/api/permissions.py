from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request,view,  obj):
        
        return obj.owner == request.user
        