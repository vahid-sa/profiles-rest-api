from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from .utils import generate_id_code


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user_profile(self, email: str, first_name: str, last_name: str, password: (str, type(None)) = None, save: bool = True):
        """Create new user profile"""
        if not email:
            raise ValueError("Each user must have an email address")
        email = self.normalize_email(email=email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        if save:
            self.save_user(user=user)
        return user

    def create_superuser(self, email: str, first_name: str, last_name: str, password: str):
        """Create and save a new superuser with given details"""
        user = self.create_user_profile(email=email, first_name=first_name, last_name=last_name, password=password, save=True)
        user.is_superuser = True
        user.is_staff = True
        self.save_user(user=user)

    def save_user(self, user):
        """save the given user in the database."""
        user.save_user(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    id_code = models.CharField(unique=True, max_length=32, default=generate_id_code)

    objects = UserProfileManager()

    USERNAME_FIELD = 'id_code'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    EMAIL_FIELD = ['email']

    def get_full_name(self) -> str:
        """Retrieve full name of the user"""
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self) -> str:
        """Retrieve short name of thr user"""
        return f"{self.first_name}"

    def get_email_field_name(self) -> str:
        """Retrieve email of the user"""
        return f"{self.email}"

    def __str__(self) -> str:
        """Return string representation of the user"""
        return f"{self.id_code}"
