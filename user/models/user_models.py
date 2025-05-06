import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from utils.managers.custom_user_manager import CustomUserManager


class User(AbstractUser):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    USER_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('librarian', 'Librarian'),
    ]


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    email = models.EmailField(_('email address'), unique=True, error_messages={
        "unique": _("A user with that Email already exists."),
    }, )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    user_type = models.CharField(max_length=10, choices=USER_CHOICES, default='student')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        """
        Returns the full name of the user by combining first and last name.
        """
        return f"{self.first_name} {self.last_name}"