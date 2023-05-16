from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
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

    basic_information_form = BasicInformationForm(instance=basic_information)
    city_planning_form = CityPlanningForm(instance=city_planning)
    building_information_form = BuildingInformationForm(instance=building_information)
    land_information_form = LandInformationForm(instance=land_information)
    infrastructure_information_form = InfrastructureInformationForm(
        instance=infrastructure_information
    )
    

    context = {
        "basic_information_form": basic_information_form,
        "city_planning_form":city_planning_form,
        "building_information_form":building_information_form,
        "land_information_form":land_information_form,
        "infrastructure_information_form":infrastructure_information_form,
    }

    return render(request, "detail.html", context)

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
            custom_user = User.objects.get(username=request.user.username)
            basic_information.user = custom_user
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

            return HttpResponseRedirect(
                reverse(
                    "RealEstate360:propertyinfo_detail",
                    kwargs={
                        "basic_information_id": basic_information.basic_information_id
                    },
                )
            )
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
        "basic_information_form":basic_information_form,
        "city_planning_form":city_planning_form,
        "building_information_form":building_information_form,
        "land_information_form":land_information_form,
        "infrastructure_information_form":infrastructure_information_form,
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
