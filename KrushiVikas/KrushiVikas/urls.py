"""KrushiVikas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authkv.views import index, usignup, ulogin, ulogout, fp, checkfpo, updatepw, ev, home
from crop_prediction.views import predict, output
from plant_disease_detection.views import plantdd, disease
from rent_tools.views import (
    tools,
    addtools,
    viewtools,
    process,
    remove,
    search,
    mytools,
)
from weather_news_api.views import weather, news
from expert_assistance.views import contact, developers, help

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("home/", home, name="home"),
    path("signup/", usignup, name="usignup"),
    path("login/", ulogin, name="ulogin"),
    path("logout/", ulogout, name="ulogout"),
    path("forgot_password/", fp, name="fp"),
    path("forgot_password_otp/", checkfpo, name="checkfpo"),
    path("update_password/", updatepw, name="updatepw"),
    path("email_verification/", ev, name="ev"),
    path("crop_prediction/", predict, name="predict"),
    path("prediction_result/", output, name="output"),
    path("plant_disease_detection/", plantdd, name="plantdd"),
    path("detected_disease/", disease, name="disease"),
    path("rent_tools/", tools, name="tools"),
    path("addtools/", addtools, name="addtools"),
    path("viewtools/", viewtools, name="viewtools"),
    path("mytools/", mytools, name="mytools"),
    path("renting_process/", process, name="process"),
    path("remove/<int:id>", remove, name="remove"),
    path("search/", search, name="search"),
    path("weather/", weather, name="weather"),
    path("news/", news, name="news"),
    path("expert_assistance/", contact, name="contact"),
    path("developers/", developers, name="developers"),
    path("help/", help, name="help"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
