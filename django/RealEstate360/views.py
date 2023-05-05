from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import (
    BasicInformationForm,
    CityPlanningForm,
    BuildingInformationForm,
    LandInformationForm,
    InfrastructureInformationForm,
)

from .models import (
    BasicInformation,
    CityPlanning,
    BuildingInformation,
    LandInformation,
    InfrastructureInformation,
)


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("RealEstate360:propertyinfos_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def propertyinfos_list(request):
    basic_informations = BasicInformation.objects.filter(is_active=True)

    context = {
        "basic_informations": basic_informations,
    }

    return render(request, "propertyinfos_list.html", context)


@login_required
def propertyinfo_detail(request, basic_information_id):
    basic_information = get_object_or_404(BasicInformation, pk=basic_information_id)
    city_planning = get_object_or_404(CityPlanning, basic_information=basic_information)
    building_information = get_object_or_404(
        BuildingInformation, basic_information=basic_information
    )
    land_information = get_object_or_404(
        LandInformation, basic_information=basic_information
    )
    infrastructure_information = get_object_or_404(
        InfrastructureInformation, basic_information=basic_information
    )

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

    building_information_exclude_fields = [
        "basic_information",
        "building_information_id",
    ]
    building_information_fields = [
        (field, field.value_from_object(building_information))
        for field in building_information._meta.fields
        if field.name not in building_information_exclude_fields
    ]

    land_information_exclude_fields = [
        "basic_information",
        "land_information_id",
    ]
    land_information_fields = [
        (field, field.value_from_object(land_information))
        for field in land_information._meta.fields
        if field.name not in land_information_exclude_fields
    ]

    infrastructure_information_exclude_fields = [
        "basic_information",
        "infrastructure_information_id",
    ]
    infrastructure_information_fields = [
        (field, field.value_from_object(infrastructure_information))
        for field in infrastructure_information._meta.fields
        if field.name not in infrastructure_information_exclude_fields
    ]

    context = {
        "basic_information": basic_information,
        "basic_information_fields": basic_information_fields,
        "city_planning_fields": city_planning_fields,
        "building_information_fields": building_information_fields,
        "land_information_fields": land_information_fields,
        "infrastructure_information_fields": infrastructure_information_fields,
    }

    return render(request, "propertyinfo_detail.html", context)


@login_required
def propertyinfo_create(request):
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

            return redirect("RealEstate360:propertyinfos_list")
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
    return render(request, "propertyinfo_create.html", context)


@login_required
def propertyinfo_edit(request, basic_information_id):
    basic_information = get_object_or_404(BasicInformation, pk=basic_information_id)
    city_planning = get_object_or_404(CityPlanning, basic_information=basic_information)
    building_information = get_object_or_404(
        BuildingInformation, basic_information=basic_information
    )
    land_information = get_object_or_404(
        LandInformation, basic_information=basic_information
    )
    infrastructure_information = get_object_or_404(
        InfrastructureInformation, basic_information=basic_information
    )

    basic_information_form = BasicInformationForm(instance=basic_information)
    city_planning_form = CityPlanningForm(instance=city_planning)
    building_information_form = BuildingInformationForm(instance=building_information)
    land_information_form = LandInformationForm(instance=land_information)
    infrastructure_information_form = InfrastructureInformationForm(
        instance=infrastructure_information
    )

    if request.method == "POST":
        basic_information_form = BasicInformationForm(
            request.POST, instance=basic_information
        )
        city_planning_form = CityPlanningForm(request.POST, instance=city_planning)
        building_information_form = BuildingInformationForm(
            request.POST, instance=building_information
        )
        land_information_form = LandInformationForm(
            request.POST, instance=land_information
        )
        infrastructure_information_form = InfrastructureInformationForm(
            request.POST, instance=infrastructure_information
        )

        # フォームがすべて有効であることを確認して、保存します。
        if (
            basic_information_form.is_valid()
            and city_planning_form.is_valid()
            and building_information_form.is_valid()
            and land_information_form.is_valid()
            and infrastructure_information_form.is_valid()
        ):
            basic_information_form.save()
            city_planning_form.save()
            building_information_form.save()
            land_information_form.save()
            infrastructure_information_form.save()

            return HttpResponseRedirect(reverse("RealEstate360:propertyinfos_list"))

    context = {
        "forms": [
            basic_information_form,
            city_planning_form,
            building_information_form,
            land_information_form,
            infrastructure_information_form,
        ],
        "basic_information": basic_information,
    }
    return render(request, "propertyinfo_edit.html", context)


@csrf_protect
def propertyinfo_inactive(request, basic_information_id):
    if request.method == "POST":
        basic_information = get_object_or_404(BasicInformation, pk=basic_information_id)
        basic_information.is_active = False
        basic_information.save()
        return redirect("/")
    else:
        return HttpResponseNotAllowed(["POST"])
