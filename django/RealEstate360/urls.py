from django.urls import path
from . import views


app_name = "RealEstate360"
urlpatterns = [
    path("", views.loginfunc, name="login"),
    path("logout/", views.logoutfunc, name="logout"),
    path("propertyinfos_list/", views.propertyinfos_list, name="propertyinfos_list"),
    path("propertyinfo_create/", views.propertyinfo_create, name="propertyinfo_create"),
    path(
        "propertyinfo_edit/<int:basic_information_id>/",
        views.propertyinfo_edit,
        name="propertyinfo_edit",
    ),
    path(
        "propertyinfo_detail/<int:basic_information_id>/",
        views.propertyinfo_detail,
        name="propertyinfo_detail",
    ),
    path(
        "propertyinfo_inactive/<int:basic_information_id>/",
        views.propertyinfo_inactive,
        name="propertyinfo_inactive",
    ),
    path("get_properties/", views.get_properties, name="get_properties"),
]
