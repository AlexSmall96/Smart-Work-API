from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Standard permissions to be used on several models
    Only owner can edit or delete
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsOwnerOrReadOnlyMember(permissions.BasePermission):
    """
    Custom permission to be used on members model
    Only project owner or profile owner can delete member
    ie. remove a user from a project
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (obj.project.owner == request.user
                or obj.profile.owner == request.user)


class IsOwnerOrReadOnlyTask(permissions.BasePermission):
    """
    Custom permission to be used on task model
    Only assigned to member can update or delete task
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (obj.assigned_to.profile.owner == request.user)
