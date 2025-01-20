from django.contrib.auth.models import (
    AbstractBaseUser,
    Group,
    Permission,
    PermissionsMixin,
)
from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from .fields import PhoneField


class UserManager(BaseUserManager):
    """
    Custom user model manager that uses email as the unique identifier
    instead of the username.
    """

    def create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""

        if not email:
            raise ValueError(_("The Email must be set"))

        if User.objects.filter(email=email).exists():
            raise Exception(User.EMAIL_ALREADY_REGISTERED_ERROR)

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_('A SuperUser must have "is_staff" set to True.'))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_('A SuperUser must have "is_superuser" set to True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    EMAIL_ALREADY_REGISTERED_ERROR = "Email already exist"

    ADMIN = "ADMIN"
    RIDER = "RIDER"
    DRIVER = "DRIVER"
    ROLE_CHOICES = [
        (ADMIN, "admin"),
        (RIDER, "rider"),
        (DRIVER, "driver"),
    ]

    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        max_length=255,
    )
    first_name = models.CharField(
        verbose_name="First name", max_length=30, default="first"
    )
    last_name = models.CharField(
        verbose_name="Last name", max_length=30, default="last"
    )
    phone = PhoneField.build(blank=True)
    role = models.CharField(
        max_length=30, choices=ROLE_CHOICES, default=None, null=True
    )
    is_admin = models.BooleanField(verbose_name="Admin", default=False)
    is_active = models.BooleanField(verbose_name="Active", default=True)
    is_staff = models.BooleanField(verbose_name="Staff", default=False)
    is_superuser = models.BooleanField(verbose_name="Superuser", default=False)

    # Audit fields
    created_by = models.CharField(verbose_name="Created by", max_length=50)
    updated_by = models.CharField(verbose_name="Updated by", max_length=50)

    # Groups
    groups = models.ManyToManyField(
        Group, verbose_name="Groups", related_name="user_groups"
    )
    user_permissions = models.ManyToManyField(
        Permission, verbose_name="Permissions", related_name="user_permissions"
    )

    # Fields settings
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                name="email",
                violation_error_message="Email already exist.",
            ),
        ]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".title()

    def __str__(self):
        return f"{self.email} | {self.full_name}"
