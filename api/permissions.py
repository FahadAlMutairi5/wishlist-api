from rest_framework.permissions import BasePermission

class IsAdd(BasePermission):
    message = "You are not the add of this items. Go away! You're naughty..."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.added_by == request.user:
            return True
        return False