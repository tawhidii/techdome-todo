from rest_framework import permissions


class IsUserOrIsAdmin(permissions.BasePermission):
    """Custom permission class for user or admin access"""
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.roles == 'user'
                    or request.user.is_authenticated and request.user.roles == 'admin')


class IsAdmin(permissions.BasePermission):
    """Custom permission class for admin access"""
    message = 'Only admin user can access !!'

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.roles == 'admin')
