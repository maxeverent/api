from django.db import models

# Create your models here.

class Cabinets(models.Model):
    number = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=20)
    days_working = models.CharField(max_length=50)
