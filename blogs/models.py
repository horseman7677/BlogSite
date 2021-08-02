from django.db import models
from datetime import datetime

# Create your models here.


class Header(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=75, blank=True)
    body = models.CharField(max_length=1000000, blank=True)
    time = models.DateTimeField(default=datetime.now, blank=True)
