from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ( 'username', 'email', 'first_name', 'last_name', 'user_type', 'is_superuser')
    filter_horizontal = 'user_permissions',
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('time_created', 'last_visit')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('time_created', 'last_login', 'last_visit')}),
    )
    save_on_top = True


admin.site.site_title = 'Admin Panel'
admin.site.site_header = 'Admin Panel'
