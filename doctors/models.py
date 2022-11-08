from django.db import models
from cabinets.models import Cabinets

# Create your models here.
class Doctors(models.Model):
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    cabinet_id = models.ForeignKey(Cabinets, on_delete=models.PROTECT, null=True)
