from django.shortcuts import render


def view_propertyinfos(request):
    # property_infos = CityPlanning.objects.select_related("basic_information").all()

    # context = {
    #    "property_infos": property_infos,
    # }

    return render(request, "view_propertyinfos.html",)  # context)


def detail(request):
    return render(request, "detail.html",)


def edit(request):
    return render(request, "edit.html", )


def lists(request):
    return render(request, "lists.html", )
