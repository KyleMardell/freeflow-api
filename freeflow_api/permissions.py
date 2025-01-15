from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        project = obj.project
        return project.owner == request.user