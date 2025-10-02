from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Gig, TaskRequest

@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'category', 'price')
    search_fields = ('title', 'description')
    list_filter = ('category',)


@admin.register(TaskRequest)
class TaskRequestAdmin(admin.ModelAdmin):
    list_display = ('category', 'location', 'seller', 'created_at')
    search_fields = ('location', 'details')
    list_filter = ('category', 'created_at')