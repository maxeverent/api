from rest_framework import viewsets
from . import models
from . import serializers

class TestCrudViewset(viewsets.ModelViewSet):
    queryset = models.TestCrud.objects.all()
    serializer_class = serializers.TestCrudSerializer