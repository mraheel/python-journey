from django.contrib import admin
from .models import Role, Permission, RolePermission

class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission')
    list_filter = ('role', 'permission')
    search_fields = ('role__name', 'permission__name')

admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(RolePermission, RolePermissionAdmin)