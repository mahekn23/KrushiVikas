from django.shortcuts import render, redirect
from rent_tools.models import RentModel
from rent_tools.form import RentForm


# Create your views here.
def tools(request):
    return render(request, "tools.html")


def addtools(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        if request.method == "POST":
            f = RentForm(request.POST, request.FILES)
            if f.is_valid():
                print(f.data["email_id"])
                if str(f.data["email_id"]) == str(user):
                    f.save()
                    fm = RentForm()
                    return render(
                        request, "addtools.html", {"fm": fm, "msg": "Tool added :)"}
                    )
                else:
                    return render(
                        request,
                        "addtools.html",
                        {"fm": f, "msg": "Use the registered email id!"},
                    )
            else:
                fm = RentForm()
                return render(
                    request, "addtools.html", {"fm": f, "msg": "Some error occured! Please check all fields."}
                )
        else:
            fm = RentForm(initial={"user": request.user})
            return render(request, "addtools.html", {"fm": fm})


def viewtools(request):
    data = RentModel.objects.all()
    return render(request, "viewtools.html", {"data": data})


def mytools(request):
    data = RentModel.objects.filter(email_id=request.user)
    return render(request, "mytools.html", {"data": data})


def process(request):
    return render(request, "process.html")


def remove(request, id):
    d = RentModel.objects.get(uid=id)
    d.delete()
    return redirect("viewtools")


def search(request):
    s = request.GET.get("search")
    data = RentModel.objects.filter(tool_name=s)
    return render(request, "viewtools.html", {"data": data})
