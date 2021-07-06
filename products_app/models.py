from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
