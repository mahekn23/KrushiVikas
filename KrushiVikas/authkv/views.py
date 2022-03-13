import email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from sympy import O
from KrushiVikas.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange

# Create your views here.
global otp
otp = ""

global fpo
fpo = ""


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def usignup(request):
    if request.method == "POST":
        un = request.POST.get("un")
        em = request.POST.get("em")
        pw1 = request.POST.get("pw1")
        pw2 = request.POST.get("pw2")
        try:
            usr = User.objects.get(username=em)
            return render(request, "usignup.html", {"msg": "User already exists!!"})
        except User.DoesNotExist:
            if pw1 == pw2:
                text = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ"
                global otp
                for i in range(6):
                    otp = otp + text[randrange(len(text))]
                print(otp)
                subject = "KrushiVikas Email Verification"
                msg = (
                    "Welcome "
                    + un
                    + ",\n"
                    + "\nWe are excited to have you as a part of pur community. \nPlease verify your email address using the OTP provided below.\n"
                    + "OTP for Email Verification: "
                    + str(otp)
                    + ".\n"
                    + "If you do have any futher queries, kindly contact us via email (krushivikas2022@gmail.com).\n"
                    + "\nIf you did not initiate this verification, please ignore this email.\n"
                    + "\nRegards,\nThe KrushiVikas Team."
                )
                send_mail(subject, msg, EMAIL_HOST_USER, [em])
                usr = User.objects.create_user(
                    username=em, password=pw1, last_name="not_verified"
                )
                usr.save()
                return render(request, "ev.html")
            else:
                return render(
                    request, "usignup.html", {"msg": "Passwords did not match!!"}
                )
    else:
        return render(request, "usignup.html")


def ulogin(request):
    if request.method == "POST":
        em = request.POST.get("em")
        pw = request.POST.get("pw")
        usr = authenticate(username=em, password=pw)
        if usr is None:
            return render(request, "ulogin.html", {"msg": "Invalid credentials!!"})
        else:
            u = User.objects.get(username=em)
            if u.last_name == "verified":
                login(request, usr)
                return redirect("home")
            else:
                return render(
                    request, "ulogin.html", {"msg": "Please verify your email"}
                )
    else:
        return render(request, "ulogin.html")


def ulogout(request):
    logout(request)
    return redirect("index")


def ev(request):
    if request.method == "POST":
        em = request.POST.get("em")
        op = request.POST.get("op")
        global otp
        if op == otp:
            usr = User.objects.get(username=em)
            if usr is not None:
                if usr.last_name == "not_verified":
                    usr.last_name = "verified"
                    print(usr.last_name)
                    usr.save()
                else:
                    return render(
                        request, "ulogin.html", {"msg": "Email is already verified!!"}
                    )
            else:
                return render(request, "ev.html", {"msg": "User does not exist!!"})
            otp = ""
            return redirect("ulogin")
        else:
            return render(request, "ev.html", {"msg": "OTP did not match!!"})
    else:
        return render(request, "ev.html")


def fp(request):
    if request.method == "POST":
        em = request.POST.get("em")
        
        try:
            usr = User.objects.get(username=em)
            if usr.last_name == "verified":
                text = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ"
                global fpo
                for i in range(6):
                    fpo = fpo + text[randrange(len(text))]
                print(fpo)
                subject = "KrushiVikas : Forgot Password"
                msg = (
                    "Hello "
                    + em
                    + ",\n"
                    + "\nWe got a forgot password request from you. \nIf you did not initiate this request, please contact us immediately.\n"
                    + "OTP for updating the password: "
                    + str(fpo)
                    + ".\n"
                    + "If you do have any futher queries, kindly contact us via email (krushivikas2022@gmail.com).\n"
                    + "\nRegards,\nThe KrushiVikas Team."
                )
                send_mail(subject, msg, EMAIL_HOST_USER, [em])
                return render(request, "checkfpo.html")
            else:
                return render(
                    request, "ulogin.html", {"msg": "Please verify your email"}
                )
        except User.DoesNotExist:
            return render(request, "fp.html", {"msg": "User does not exist!"})
    else:
        return render(request, "fp.html")


def checkfpo(request):
    if request.method == "POST":
        fpo1 = request.POST.get("fpo")
        try:
            global fpo
            if fpo1 == fpo:
                fpo = ""
                return render(request, "updatepw.html")
            else:
                return render(request, "checkfpo.html", {"msg": "OTPs did not match!"})
        except:
            return render(request, "checkfpo.html", {"msg": "Some error occured!"})
    else:
        return render(request, "checkfpo.html")


def updatepw(request):
    if request.method == "POST":
        em = request.POST.get("em")
        pw1 = request.POST.get("pw1")
        pw2 = request.POST.get("pw2")
        if pw1 == pw2:
            try:
                usr = User.objects.get(username=em)
                usr.set_password(pw1)
                usr.save()
                return render(
                    request,
                    "ulogin.html",
                    {
                        "msg": "Your password was updated, please login with a new password."
                    },
                )
            except:
                return render(request, "updatepw.html", {"msg": "Some error occured!"})
        else:
            return render(
                request,
                "updatepw.html",
                {"msg": "Passwords did not match, try again!"},
            )
    else:
        return render(request, "updatepw.html")
