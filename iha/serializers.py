from rest_framework import serializers
from .models import Iha

class IhaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Iha
        fields = '__all__'
        
