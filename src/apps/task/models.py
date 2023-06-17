from django.db import models

from apps.user.models import User
from project.models import BaseModel


class Task(BaseModel):
    user = models.ForeignKey(User, related_name='tasks', verbose_name='User', on_delete=models.CASCADE)
    header = models.CharField(max_length=255, verbose_name='Header')
    description = models.TextField(verbose_name='Description')
    completed = models.BooleanField(default=False, verbose_name='Completed')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
