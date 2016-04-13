from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, email,password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True) #Needs to be unique for login
    username = models.CharField(max_length=32, unique=True) #Needs to be unique for URL

    first_name = models.CharField(max_length=32, blank=True)
    second_name = models.CharField(max_length=32, blank=True)
    tagline = models.CharField(max_length=128,blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True) #When object was created
    updated_at = models.DateTimeField(auto_now=True) #When object was last updated

    objects = AccountManager()

    USERNAME_FIELD = 'email' #Djangos built in user requires a username. This is used to log in the user.
    REQUIRED_FIELDS = ['username'] #will need to use username in URL so we must have it.

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
