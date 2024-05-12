from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RentalOperationSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import RentalOperation
from django.db.models import Q


class RentalOperationListCreate(generics.ListCreateAPIView):
    queryset = RentalOperation.objects.all()
    serializer_class = RentalOperationSerializer
    permission_classes =[AllowAny]

    def get_queryset(self):
       
       
        queryset = RentalOperation.objects.all()

        #/api/iha/?from=2022-01-01&to=2022-12-31
        startDate = self.request.query_params.get('from', None)
        endDate = self.request.query_params.get('to', None)
        brand = self.request.query_params.get('brand', None)
        model = self.request.query_params.get('model', None)
        id = self.request.query_params.get('iha_id', None)
        category = self.request.query_params.get('category', None)

        #endDate ve startdate aralığında bir fltreleme yapman lazım Q kullanarak
        if startDate and endDate:
            queryset = queryset.filter(Q(rental_date__gte=startDate) & Q(rental_date__lte=endDate))

        if brand:
            queryset = queryset.filter(iha__brand__icontains=brand)
        
        if model:
            queryset = queryset.filter(iha__model__icontains=model)
        
        if id:
            queryset = queryset.filter(iha__id=id)
        

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

    
    


