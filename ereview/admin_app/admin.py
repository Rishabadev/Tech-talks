from django.contrib import admin
from .models import Category,Product,Review

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)

from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser  # Only superadmin can manage users


