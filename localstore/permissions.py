from rest_framework import permissions

from accounts.models import CustomUser


class IsWarehouseAttendeeOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        warehouse_attendees = CustomUser.objects.filter(role="W")
        warehouse_attendees_emails = [
            warehouse_attendee.email for warehouse_attendee in warehouse_attendees
        ]
        # Write permissions are only allowed to the warehouse attendees

        return request.user in warehouse_attendees_emails
