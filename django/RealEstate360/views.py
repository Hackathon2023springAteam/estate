from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render, redirect
from .forms import (
    BasicInformationForm,
    CityPlanningForm,
    BuildingInformationForm,
    LandInformationForm,
    InfrastructureInformationForm,
)

from .models import BasicInformation, CityPlanning


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("RealEstate360:view_propertyinfos")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def view_propertyinfos(request):
    basic_informations = BasicInformation.objects.all()

    context = {
        "basic_informations": basic_informations,
    }

    return render(request, "view_propertyinfos.html", context)


@login_required
def propertyinfo_detail(request, basic_information_id):
    basic_information = get_object_or_404(BasicInformation, pk=basic_information_id)
    city_planning = get_object_or_404(CityPlanning, basic_information=basic_information)

    basic_information_exclude_fields = ["basic_information_id", "user"]
    basic_information_fields = [
        (field, field.value_from_object(basic_information))
        for field in basic_information._meta.fields
        if field.name not in basic_information_exclude_fields
    ]

    city_planning_exclude_fields = ["basic_information", "city_planning_id"]
    city_planning_fields = [
        (field, field.value_from_object(city_planning))
        for field in city_planning._meta.fields
        if field.name not in city_planning_exclude_fields
    ]

    context = {
        "basic_information": basic_information,
        "basic_information_fields": basic_information_fields,
        "city_planning_fields": city_planning_fields,
    }

    return render(request, "propertyinfo_detail.html", context)


@login_required
def create_propertyinfo(request):
    if request.method == "POST":
        basic_information_form = BasicInformationForm(request.POST)
        city_planning_form = CityPlanningForm(request.POST)
        building_information_form = BuildingInformationForm(request.POST)
        land_information_form = LandInformationForm(request.POST)
        infrastructure_information_form = InfrastructureInformationForm(request.POST)

        if (
            basic_information_form.is_valid()
            and city_planning_form.is_valid()
            and building_information_form.is_valid()
            and land_information_form.is_valid()
            and infrastructure_information_form.is_valid()
        ):
            basic_information = basic_information_form.save(commit=False)
            basic_information.user = request.user
            basic_information.save()

            city_planning = city_planning_form.save(commit=False)
            city_planning.basic_information = basic_information
            city_planning.save()

            building_information = building_information_form.save(commit=False)
            building_information.basic_information = basic_information
            building_information.save()

            land_information = land_information_form.save(commit=False)
            land_information.basic_information = basic_information
            land_information.save()

            infrastructure_information = infrastructure_information_form.save(
                commit=False
            )
            infrastructure_information.basic_information = basic_information
            infrastructure_information.save()

            return redirect("RealEstate360:view_propertyinfos")
    else:
        basic_information_form = BasicInformationForm()
        city_planning_form = CityPlanningForm()
        building_information_form = BuildingInformationForm()
        land_information_form = LandInformationForm()
        infrastructure_information_form = InfrastructureInformationForm()

    context = {
        "basic_information_form": basic_information_form,
        "city_planning_form": city_planning_form,
        "building_information_form": building_information_form,
        "land_information_form": land_information_form,
        "infrastructure_information_form": infrastructure_information_form,
    }
    return render(request, "create_propertyinfo.html", context)
