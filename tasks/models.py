from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateField(default=date.today)
    completed=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self) -> str:
        return self.title

    
