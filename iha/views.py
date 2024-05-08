from django.shortcuts import render
from rest_framework import generics
from .serializers import IhaSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Iha   


class IhaListCreate(generics.ListCreateAPIView):  
    serializer_class = IhaSerializer
    permission_classes =[AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Iha.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        
        

class IhaDelete(generics.DestroyAPIView):
    queryset = Iha.objects.all()
    serializer_class = IhaSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Iha.objects.all()
        
    
    

    

