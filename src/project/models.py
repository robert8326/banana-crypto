from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    update = models.DateTimeField(auto_now=True, verbose_name='Update')

    class Meta:
        abstract = True
