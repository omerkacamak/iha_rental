from rest_framework import serializers
from .models import RentalOperation


class RentalOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalOperation
        fields = '__all__'
        