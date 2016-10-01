from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.http import urlquote
from django.core.mail import send_mail

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):

    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(blank=True, unique=True)
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    company_name = models.CharField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=32, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=None, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', 'company_name')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return '/users/%s/' % urlquote(self.username)

    def get_full_name(self):
        """
        Return the first_name plus the last name, with a space in between
        :return: string
        """
        return " ".join((self.first_name, self.last_name)).strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        :return:
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this user.
        :param subject: string
        :param message: string
        :param from_email: boolean
        :return:
        """
        send_mail(subject, message, from_email, [self.email])

