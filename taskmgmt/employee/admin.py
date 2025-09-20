from django.contrib import admin
from .models import Employee
from task.models import Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
