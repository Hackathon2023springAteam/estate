from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from decimal import Decimal
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
    User,
)


def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("RealEstate360:propertyinfos_list")
        else:
            # エラーメッセージを表示するなど、認証に失敗した場合の処理を追加できます
            pass

    return render(request, "login.html", {})


def logoutfunc(request):
    logout(request)
    return redirect("RealEstate360:login")


@login_required
def propertyinfos_list(request):
    basic_informations = BasicInformation.objects.filter(is_active=True)

    context = {
        "basic_informations": basic_informations,
    }

    return render(request, "list.html", context)


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

    return render(request, "detail.html", context)


@login_required
def propertyinfo_create(request):
    basic_information_labels = {
        "control_number": BasicInformation._meta.get_field(
            "control_number"
        ).verbose_name,
        "property_name": BasicInformation._meta.get_field("property_name").verbose_name,
        "location": BasicInformation._meta.get_field("location").verbose_name,
        "address": BasicInformation._meta.get_field("address").verbose_name,
    }

    city_planning_labels = {
        "zoning": CityPlanning._meta.get_field("zoning").verbose_name,
        "public_land_expansion_act": CityPlanning._meta.get_field(
            "public_land_expansion_act"
        ).verbose_name,
        "road_width": CityPlanning._meta.get_field("road_width").verbose_name,
        "condition": CityPlanning._meta.get_field("condition").verbose_name,
    }

    building_information_labels = {
        "certified_copy_of_building": BuildingInformation._meta.get_field(
            "certified_copy_of_building"
        ).verbose_name,
        "building_drawing": BuildingInformation._meta.get_field(
            "building_drawing"
        ).verbose_name,
        "building_confirmation_screen": BuildingInformation._meta.get_field(
            "building_confirmation_screen"
        ).verbose_name,
        "property_tax_assessment_certificate": BuildingInformation._meta.get_field(
            "property_tax_assessment_certificate"
        ).verbose_name,
        "building_use": BuildingInformation._meta.get_field(
            "building_use"
        ).verbose_name,
        "type_of_rights": BuildingInformation._meta.get_field(
            "type_of_rights"
        ).verbose_name,
        "relationship_to_land_owner": BuildingInformation._meta.get_field(
            "relationship_to_land_owner"
        ).verbose_name,
    }

    land_information_labels = {
        "area": LandInformation._meta.get_field("area").verbose_name,
        "square_meter": LandInformation._meta.get_field("square_meter").verbose_name,
        "land_category": LandInformation._meta.get_field("land_category").verbose_name,
        "certified_copy_of_land": LandInformation._meta.get_field(
            "certified_copy_of_land"
        ).verbose_name,
        "character_map": LandInformation._meta.get_field("character_map").verbose_name,
        "survey_map": LandInformation._meta.get_field("survey_map").verbose_name,
        "type_of_rights": LandInformation._meta.get_field(
            "type_of_rights"
        ).verbose_name,
    }

    infrastructure_information_labels = {
        "water_supply": InfrastructureInformation._meta.get_field(
            "water_supply"
        ).verbose_name,
        "sweage": InfrastructureInformation._meta.get_field("sweage").verbose_name,
        "solar_power_generation": InfrastructureInformation._meta.get_field(
            "solar_power_generation"
        ).verbose_name,
    }

    context = {
        "basic_information_labels": basic_information_labels,
        "city_planning_labels": city_planning_labels,
        "building_information_labels": building_information_labels,
        "land_information_labels": land_information_labels,
        "infrastructure_information_labels": infrastructure_information_labels,
    }

    if request.method == "POST":
        # about BasicInformation
        basic_information_control_number = request.POST.get(
            "basic_information_control_number"
        )
        basic_information_property_name = request.POST.get(
            "basic_information_property_name"
        )
        basic_information_location = request.POST.get("basic_information_location")
        basic_information_address = request.POST.get("basic_information_address")

        basic_information = BasicInformation.objects.create(
            user=request.user,
            control_number=basic_information_control_number,
            property_name=basic_information_property_name,
            location=basic_information_location,
            address=basic_information_address,
        )

        # about CitiPlanning
        city_planning_zoning = request.POST.get("city_planning_zoning")
        city_planning_public_land_expansion_act = request.POST.get(
            "city_planning_public_land_expansion_act"
        )
        city_planning_road_width = Decimal(request.POST.get("city_planning_road_width"))
        city_planning_condition = request.POST.get("city_planning_condition")

        city_planning = CityPlanning.objects.create(
            basic_information=basic_information,
            zoning=city_planning_zoning,
            public_land_expansion_act=city_planning_public_land_expansion_act,
            road_width=city_planning_road_width,
            condition=city_planning_condition,
        )

        # about BuildingInformation
        building_information_certified_copy_of_building = request.POST.get(
            "building_information_certified_copy_of_building"
        )
        building_information_building_drawing = request.POST.get(
            "building_information_building_drawing"
        )
        building_information_building_confirmation_screen = request.POST.get(
            "building_information_building_confirmation_screen"
        )
        building_information_property_tax_assessment_certificate = request.POST.get(
            "building_information_property_tax_assessment_certificate"
        )
        building_information_building_use = request.POST.get(
            "building_information_building_use"
        )
        building_information_type_of_rights = request.POST.get(
            "building_information_type_of_rights"
        )
        building_information_relationship_to_land_owner = request.POST.get(
            "building_information_relationship_to_land_owner"
        )
        building_information = BuildingInformation.objects.create(
            basic_information=basic_information,
            certified_copy_of_building=building_information_certified_copy_of_building,
            building_drawing=building_information_building_drawing,
            building_confirmation_screen=building_information_building_confirmation_screen,
            property_tax_assessment_certificate=building_information_property_tax_assessment_certificate,
            building_use=building_information_building_use,
            type_of_rights=building_information_type_of_rights,
            relationship_to_land_owner=building_information_relationship_to_land_owner,
        )

        # about LandInformation
        land_information_area = float(request.POST.get("land_information_area"))
        land_information_square_meter = float(
            request.POST.get("land_information_square_meter")
        )
        land_information_land_category = int(
            request.POST.get("land_information_land_category")
        )
        land_information_certified_copy_of_land = request.POST.get(
            "land_information_certified_copy_of_land"
        )
        land_information_character_map = request.POST.get(
            "land_information_character_map"
        )
        land_information_survey_map = request.POST.get("land_information_survey_map")
        land_information_type_of_rights = request.POST.get(
            "land_information_type_of_rights"
        )

        land_information = LandInformation.objects.create(
            basic_information=basic_information,
            area=land_information_area,
            square_meter=land_information_square_meter,
            land_category=land_information_land_category,
            certified_copy_of_land=land_information_certified_copy_of_land,
            character_map=land_information_character_map,
            survey_map=land_information_survey_map,
            type_of_rights=land_information_type_of_rights,
        )

        # about InfrastructureInformation
        infrastructure_information_water_supply = request.POST.get(
            "infrastructure_information_water_supply"
        )
        infrastructure_information_sweage = request.POST.get(
            "infrastructure_information_sweage"
        )
        infrastructure_information_solar_power_generation = int(
            request.POST.get("infrastructure_information_solar_power_generation")
        )

        infrastructure_information = InfrastructureInformation.objects.create(
            basic_information=basic_information,
            water_supply=infrastructure_information_water_supply,
            sweage=infrastructure_information_sweage,
            solar_power_generation=infrastructure_information_solar_power_generation,
        )

        return HttpResponseRedirect(
            reverse(
                "RealEstate360:propertyinfo_detail",
                kwargs={"basic_information_id": basic_information.basic_information_id},
            )
        )

    else:
        return render(request, "create.html", context)


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
            return HttpResponseRedirect(
                reverse(
                    "RealEstate360:propertyinfo_detail",
                    kwargs={
                        "basic_information_id": basic_information.basic_information_id
                    },
                )
            )

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
    return render(request, "edit.html", context)


@csrf_protect
def propertyinfo_inactive(request, basic_information_id):
    if request.method == "POST":
        basic_information = get_object_or_404(BasicInformation, pk=basic_information_id)
        basic_information.is_active = False
        basic_information.save()
        return redirect("/")
    else:
        return HttpResponseNotAllowed(["POST"])
