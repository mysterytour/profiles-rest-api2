from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #safe dont make changes
            return True #can see other users info but not make changes

        return obj.id == request.user.id
        #checking that requested profile matches logged in user
