from rest_framework import viewsets
from . import models
from . import serializers

class CabinetsViewset(viewsets.ModelViewSet):
    queryset = models.Cabinets.objects.all()
    serializer_class = serializers.CabinetsSerializer