from rest_framework import serializers
from .models import BackCall

class BackCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackCall
        fields = '__all__'