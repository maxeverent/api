from rest_framework import viewsets
from . import models
from . import serializers

class BackCallViewset(viewsets.ModelViewSet):
    queryset = models.BackCall.objects.all()
    serializer_class = serializers.BackCallSerializer