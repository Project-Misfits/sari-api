from django.db import models


# Create your models here.
class Categories(models.Model):
    # models.ForeignKey(
    #     'model.User',
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True
    # )
    # add when the user's model is added
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Products(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=True)
    categories = models.ManyToManyField(Categories)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'products'
