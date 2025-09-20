from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    searchable_fields = ('name',)
    list_filter = ('department',)