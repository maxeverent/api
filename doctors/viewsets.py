from rest_framework import viewsets
from . import models
from . import serializers

class DoctorsViewset(viewsets.ModelViewSet):
    queryset = models.Doctors.objects.all()
    serializer_class = serializers.DoctorsSerializer