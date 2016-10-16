from datetime import datetime
from django.contrib.auth.base_user import BaseUserManager

from crm.models import UserCompany, UserCompanyConnection


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, company_name=None, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        if company_name:
            company = UserCompany(
                name=company_name,
                created_by=user
            )
            company.save()

            UserCompanyConnection(
                user_id = user,
                company_id = company
            ).save()

        return user

    def create_user(self, username, email=None, password=None, company_name=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, company_name, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
