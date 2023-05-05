from django.shortcuts import render

def view_propertyinfos(request):
    #property_infos = CityPlanning.objects.select_related("basic_information").all()

    #context = {
    #    "property_infos": property_infos,
    #}

    return render(request, "view_propertyinfos.html",)# context)