import uuid

from django.db import models
from users.models import User


class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.EmailField(max_length=255, unique=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    deleted_on = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class StoreTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.EmailField(max_length=255, unique=True)
    qr_code_base64 = models.TextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    deleted_on = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
