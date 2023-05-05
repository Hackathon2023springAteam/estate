from django.urls import path
# from . import views
from .views import view_propertyinfos, detail, edit, lists

app_name = "RealEstate360"
urlpatterns = [
    path("view_propertyinfos/", view_propertyinfos, name="view_propertyinfos"),
    path("detail/", detail, name="detail"),
    path("edit/", edit, name="edit"),
    path("lists/", lists, name="lists"),
]
