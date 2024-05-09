from django.urls import path
from . import views


urlpatterns = [
    path("iha/",views.IhaListCreate.as_view(),name="iha-list"),
    path("iha/<int:id>/",views.IhaRetrieveUpdateDestroy.as_view(),name="iha-retrieve-update-destroy"),
]
