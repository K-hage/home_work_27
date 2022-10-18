from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=300)
    is_published = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
