from django.db import models
from instructor.models import Instructor

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    credits = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_code} - {self.title}"
    
    def enrolled_students_count(self):
        return self.enrollment_set.count()