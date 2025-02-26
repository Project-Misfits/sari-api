import uuid

from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

ALLOWED_GROUPS = ['admin', 'user', 'manager', 'owner']


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password=None, group_name='user'):
        if not email:
            raise ValueError('User should have an email address.')

        user = self.model(
            email=self.normalize_email(email).lower(),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        if group_name in ALLOWED_GROUPS:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password, group_name='admin'):
        user = self.create_user(email.lower(), first_name, last_name, f'admin-{uuid.uuid4()}', password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        if group_name in ALLOWED_GROUPS:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    deleted_on = models.DateTimeField(blank=True, null=True, default=None)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
