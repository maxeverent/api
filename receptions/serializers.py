from rest_framework import serializers
from .models import Receptions

class ReceptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptions
        fields = '__all__'