from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    model = Users
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_image', 'bio', 'is_seller', 'skills')}),
    )
    list_display = ('username', 'email', 'is_seller', 'skills')