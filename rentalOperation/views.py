from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RentalOperationSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import RentalOperation



class RentalOperationListCreate(generics.ListCreateAPIView):
    queryset = RentalOperation.objects.all()
    serializer_class = RentalOperationSerializer
    permission_classes =[AllowAny]

    def get_queryset(self):
        user = self.request.user
        queryset = RentalOperation.objects.all()
        user_id = self.request.query_params.get('xx', None)
        print("Onemliiiii")
        print(user_id)
        # if user_id:  
        #     queryset = queryset.filter(user_id=user_id)
        
        return queryset
        
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

    
class RentalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = RentalOperationSerializer
    permission_classes =[AllowAny]

    def get_object(self):
        return RentalOperation.objects.get(id=self.kwargs['id'])

    
    
