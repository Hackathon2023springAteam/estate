from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


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
    # property_infos = CityPlanning.objects.select_related("basic_information").all()

    # context = {
    #    "property_infos": property_infos,
    # }

    return render(
        request,
        "view_propertyinfos.html",
    )  # context)
