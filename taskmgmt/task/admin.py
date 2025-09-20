from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('status',)
    list_display = ('title', 'employee', 'status', 'days_left')
