from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        """Util function to expedite validating and creating super users."""
        if not email:
            raise ValueError('Users must have an e-mail address!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(models.Model):
    """Base user model."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, BaseUser, PermissionsMixin):
    """Super user used for internal use-only."""
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
