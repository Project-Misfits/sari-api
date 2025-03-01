import uuid

from django.db import models

from stores.models import Store


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    deleted_on = models.DateTimeField(blank=True, null=True, default=None)
