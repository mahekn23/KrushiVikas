from django.shortcuts import render
import sys
from subprocess import run, PIPE

# Create your views here.
def predict(request):
    context = {"variable": "this is sent"}
    return render(request, "crop_prediction.html")


def output(request):
    try:
        N = request.POST.get("N")
        P = request.POST.get("P")
        K = request.POST.get("K")
        temp = request.POST.get("temp")
        humidity = request.POST.get("humidity")
        ph = request.POST.get("ph")
        rain = request.POST.get("rain")

        ans = run(
            [sys.executable, "crop_rec.py", N, P, K, temp, humidity, ph, rain],
            shell=False,
            stdout=PIPE,
        )

        lines = ans.stdout.decode("utf-8")
        acc = lines[:48]
        crop = lines[53:-4]

        context = {
            "ans": crop,
            "acc": acc,
        }

        return render(request, "result.html", context)
    except:
        return render(request, "crop_prediction.html", {"msg": "Some error occured!"})


def contact(request):
    return render(request, "contact_us.html")
