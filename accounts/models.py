from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.http import urlquote
from django.core.mail import send_mail

from accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser):

    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(blank=True, unique=True)
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    company_id = models.ForeignKey("crm.UserCompany", blank=True, null=True)
    phone_number = models.CharField(max_length=32, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=None, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):              # __unicode__ on Python 2
        return self.email

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

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def set_company_id(self, id):
        self.company_id = id
