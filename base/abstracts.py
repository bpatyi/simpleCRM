from django.db import models


class AbstractBaseModel(models.Model):

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    class Meta:
        abstract = True


class CleanableModel(models.Model):

    is_valid = models.BooleanField(default=False)
    is_cleansed = models.BooleanField(default=False)

    class Meta:
        abstract = True
