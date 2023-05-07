from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout

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

def loginfunc(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        return redirect('lists')        
        # if user is not None:
        #     login(request, user)
        #     return redirect('login')
        # else:
        #     return redirect('lists')

    return render(request,'login.html', {})
