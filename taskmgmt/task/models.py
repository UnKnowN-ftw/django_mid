from django.db import models
from datetime import date
from employee.models import Employee

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

    def days_left(self):
        return (self.due_date - date.today()).days

    def prevent_assign(self):
        if self.status == 'Pending':
            pending_task_count = Task.objects.filter(employee=self.employee, status='Pending').exclude(id=self.id).count()
            if pending_task_count >= 5:
                from django.core.exceptions import ValidationError
                raise ValidationError("This employee already has 5 pending tasks.")