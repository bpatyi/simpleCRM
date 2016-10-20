from django.db import models
from django.utils import timezone


class AbstractBaseModel(models.Model):

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    class Meta:
        abstract = True