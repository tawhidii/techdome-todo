import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.db import models


class UserManager(BaseUserManager):
    """`User` model manager definition """

    def create_user(self, username, email, first_name, last_name, roles, password=None):
        """Create and return a `User` """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username,
                          email=self.normalize_email(email),
                          first_name=first_name, last_name=last_name,
                          roles=roles)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, first_name, last_name, roles, password):
        """
        Create and return a `User` with superuser permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username=username, email=email,
                                first_name=first_name, last_name=last_name, roles=roles, password=password)
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model definition for `User`
    """
    ADMIN = 'admin'
    MANAGER = 'manager'
    USER = 'user'
    ROLES_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (USER, 'User')
    )
    username = models.CharField(db_index=True, max_length=100, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    roles = models.CharField(max_length=8, choices=ROLES_CHOICES, blank=True, default=USER)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'roles']

    def __str__(self):
        """
        Returns a string representation of `User`
        """
        return self.email

    @property
    def is_staff(self):
        return self.roles
