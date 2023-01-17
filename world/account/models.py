from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from . Managers import CustomUserManager
import uuid

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    ''' creating the custom user model by overridding the default django user model'''
    password = None
    email = models.EmailField(_('Email'), max_length=255, primary_key=True)
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Mobile_number = models.CharField(max_length=10,unique=True, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    Mobile_number=models.CharField(max_length=10, unique=True)
    otp=models.CharField(max_length=4)
    uid=models.CharField(default=f'{uuid.uuid4}',max_length=200)

    def __str__(self):
        return str(self.otp)