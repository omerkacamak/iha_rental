from django.urls import path
from . import views

urlpatterns = [
    path("rentaloperation/",views.RentalOperationListCreate.as_view(),name="rentaloperation-list"),
    path('rentaloperation/<int:id>/', views.RentalRetrieveUpdateDestroy.as_view(), name='rental-retrieve-update-destroy'), 

]
