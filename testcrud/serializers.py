from rest_framework import serializers
from .models import TestCrud

class TestCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCrud
        fields = '__all__'
