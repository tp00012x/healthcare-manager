from rest_framework.permissions import BasePermission


class APIPermission(BasePermission):
    """
    Stub for permission class for API Endpoints
    """

    allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        allow_request = True  # Stub for more permissions based logic
        return request.method in self.allowed_methods and allow_request
