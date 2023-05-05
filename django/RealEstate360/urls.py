from django.urls import path
from . import views

app_name = "RealEstate360"
urlpatterns = [
    path("", views.view_propertyinfos, name="view_propertyinfos"),
]