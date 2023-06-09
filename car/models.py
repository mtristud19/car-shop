from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'
        ordering = ['name']

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    content = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'car'
        ordering = ['name']