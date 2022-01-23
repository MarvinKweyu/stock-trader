from django.contrib import admin
from accounts.models import CustomUser

# Register your models here.

# admin.site.register(CustomUser)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin interface for CustomUser
    """
    list_display = ('email', 'username',
                    'is_active', 'is_staff', 'date_joined', 'role')
    list_filter = ('is_active', 'is_staff', 'date_joined', 'role')
    search_fields = ('username', 'email')
