from rest_framework import viewsets
from . import models
from . import serializers

class ReceptionsViewset(viewsets.ModelViewSet):
    queryset = models.Receptions.objects.all()
    serializer_class = serializers.ReceptionsSerializer