from django.db import models
from datetime import datetime

# Create your models here.

class Form(models.Model):
    stuid  = models.IntegerField()
    stuname = models.CharField(max_length=100)
    sturoll = models.IntegerField()
    stumail = models.EmailField()
    stupass = models.CharField(max_length=50)
    datetime = models.DateTimeField(default=datetime.now())

class Formvalidation(models.Model):
    n = models.CharField(max_length=200)
    m = models.EmailField(max_length=200)
    p = models.CharField(max_length=100)