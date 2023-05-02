from django.urls import path
from . import views

app_name = "RealEstate360"
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("", views.view_propertyinfos, name="view_propertyinfos"),
]
