from django.db import models
from doctors.models import Doctors

# Create your models here.
class Receptions(models.Model):
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    doctor_id = models.ForeignKey(to=Doctors, related_name="doctor", on_delete=models.PROTECT, null=True)
    date = models.CharField(max_length=50)
    auth_token = models.CharField(max_length=100)