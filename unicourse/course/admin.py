from django.contrib import admin
from .models import Course
from enrollment.models import Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'title', 'instructor', 'enrolled_students_count')
    inlines = [EnrollmentInline]
