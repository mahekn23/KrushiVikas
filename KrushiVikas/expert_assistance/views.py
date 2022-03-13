from django.shortcuts import render
from KrushiVikas.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == "POST":
        try:
            n = request.POST.get("n")
            e = request.POST.get("e")
            s = request.POST.get("s")
            t = request.POST.get("t")
            subject = "KrushiVikas Feedback Message"
            msg = (
                "Hello "
                + n
                + ",\nThank you for your feedback!\n"
                + "\nOur team received the following message:\nSubject: "
                + s
                + "\nMessage: "
                + t
                + "\n\nIf you do have any futher queries, kindly contact us via email (krushivikas2022@gmail.com).\n"
                + "\nRegards,\nThe KrushiVikas Team."
            )
            send_mail(subject, msg, EMAIL_HOST_USER, [e])
            subject = "KrushiVikas Feedback Message"
            msg = (
                "User "
                + n
                + ", "
                + e
                + " sent a feedback message.\n"
                + "\nSubject: "
                + s
                + "\nMessage: "
                + t
            )
            send_mail(subject, msg, e, [EMAIL_HOST_USER])
            return render(request, "contact_us.html", {"msg": "Feedback sent!"})
        except:
            return render(request, "contact_us.html", {"msg": "Some error occured! Please email your queries."})
    else:
        return render(request, "contact_us.html")


def developers(request):
    return render(request, "developers.html")

def help(request):
    return render(request, "help.html")
