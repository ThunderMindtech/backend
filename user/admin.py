from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin interface for the custom User model with email as username."""

    # Fields to display in the admin list view
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

    # Fieldsets for the edit form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        # Add custom fields section when you add them
        # (_('Additional info'), {'fields': ('phone_number', 'date_of_birth', 'is_verified')}),
    )

    # Fieldsets for the add form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        (_('Personal info'), {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name'),
        }),
    )
