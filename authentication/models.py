from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.db.models import Q

import os

def get_image_path(instance, filename):
    return os.path.join('avatars', str(instance.id), filename)

class AccountManager(BaseUserManager):
    def create_user(self, email,password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        if not kwargs.get('first_name'):
            first_name = ''

        if not kwargs.get('last_name'):
            last_name = ''

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username'),
            first_name=kwargs.get('first_name'), second_name=kwargs.get('last_name')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account

    def find_users_by_name(self, query):
        qs = Account.objects.all()
        for term in query.split():
            qs = qs.filter(Q(first_name__icontains = term) |
                           Q(second_name__icontains = term)|
                           Q(username__icontains = term))
        return qs

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True) #Needs to be unique for login
    username = models.CharField(max_length=32, unique=True) #Needs to be unique for URL

    first_name = models.CharField(max_length=32, blank=True)
    second_name = models.CharField(max_length=32, blank=True)

    avatar = ImageField(upload_to=get_image_path, blank=True, null=True)

    is_admin = models.BooleanField(default=False) # Are they an admin?
    created_at = models.DateTimeField(auto_now_add=True) #When object was created
    updated_at = models.DateTimeField(auto_now=True) #When object was last updated

    objects = AccountManager()

    USERNAME_FIELD = 'email' #Djangos built in user requires a username. This is used to log in the user.
    REQUIRED_FIELDS = ['username'] #uses username in URL so we must have it.

    def __str__(self):
        return self.username

    def set_avatar(self):
        pass

    def get_full_name(self):
        return ' '.join([self.first_name, self.second_name])

    def get_short_name(self):
        return self.first_name

def get_anonymous_user_instance(User):
    return User(username='Anonymous',
                first_name='Anonymous',
                second_name='User')
