from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Base permission to check if the request user is the object owner
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsProjectOwner(permissions.BasePermission):
    """
    Base permission to check if the request user is the project owner
    """
    def has_object_permission(self, request, view, obj):
        project = obj.project
        return project.owner == request.user
