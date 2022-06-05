from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Schedule(models.Model):

    time = models.TimeField(max_length=100)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    day = models.ForeignKey('Day', on_delete=models.CASCADE, related_name='schedules')
    
    def __str__(self):
        return self.content


class Day(models.Model):

    date = models.DateField(max_length=100)
    memo = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return str(self.date)

        