from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfile(BasePermission):
    """Allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is the owner"""
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id
