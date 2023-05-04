from django.urls import path
from . import views

app_name = "RealEstate360"
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("", views.view_propertyinfos, name="view_propertyinfos"),
    path("create_propertyinfo/", views.create_propertyinfo, name="create_propertyinfo"),
    path(
        "propertyinfo_detail/<int:basic_information_id>",
        views.propertyinfo_detail,
        name="propertyinfo_detail",
    ),
]
