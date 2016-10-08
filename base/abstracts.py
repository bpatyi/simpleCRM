from django.db import models


class AbstractBaseModel(models.Model):
    id = models.IntegerField(verbose_name='Identifier', primary_key=True)

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    class Meta:
        abstract = True