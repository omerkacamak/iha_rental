from django.urls import path
from . import views


urlpatterns = [
    path("iha/",views.IhaListCreate.as_view(),name="iha-list"),
    path("iha/delete/<int:pk>/",views.IhaDelete.as_view(),name="iha-delete"),
]
