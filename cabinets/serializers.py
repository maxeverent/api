from rest_framework import serializers
from .models import Cabinets

class CabinetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinets
        fields = '__all__'