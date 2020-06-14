from django.db import models


class Apple(models.Model):
    name = models.CharField('品種名', max_length=30, unique=True)


class AppleJsonOnly(models.Model):
    name = models.CharField('品種名', max_length=30, unique=True)
