from rest_framework import serializers
from .models import RentalOperation
from iha.serializers import IhaSerializer


class RentalOperationSerializer(serializers.ModelSerializer):
    
    

    
    class Meta:
        model = RentalOperation
        fields = '__all__'
        
