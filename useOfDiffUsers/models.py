from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.db.models.fields import BooleanField
# Create your models here.

class Custom_manager(BaseUserManager):

    def create_superuser(self, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', False)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff = True.')

        # if other_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must be assigned to is_superuser = True.')

        return self.create_user(user_name, password, **other_fields)



    def create_user(self, user_name, password, **other_fields):

        if not user_name:
            raise ValueError("you must provide an user_name")
        user = self.model(user_name=user_name, **other_fields)

        user.set_password(password)
        user.save()
        return user

class New_user(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=16)
    is_staff = models.BooleanField(default=False)
    is_active = BooleanField(default=False)

    objects = Custom_manager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELD = ['password']

    def __str__(self):
        return self.user_name
