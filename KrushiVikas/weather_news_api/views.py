from django.shortcuts import render
import requests

# Create your views here.
def weather(request):
    if request.method == "POST":
        try:
            city = request.POST.get("city")
            a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
            a2 = "&q=" + city
            a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
            wa = a1 + a2 + a3
            res = requests.get(wa)
            data = res.json()
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            icon = (
                "http://api.openweathermap.org/img/w/"
                + data["weather"][0]["icon"]
                + ".png"
            )
            msg = (
                "Temperature of "
                + city
                + " is "
                + str(temp)
                + " degree celsius and the city has "
                + str(desc)
            )
            return render(request, "weather.html", {"msg": msg, "icon": icon})
        except Exception as e:
            return render(request, "weather.html", {"msg": "City not found"})

    else:
        return render(request, "weather.html")


def news(request):
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=b374a1780b4847db94035413c2643ed1"
    response = requests.get(url)
    data = response.json()
    list = data["articles"]
    headlines, links = [], []
    for i in list:
        headlines.append(i["title"])
        links.append(i["url"])
    return render(request, "news.html", {"h": headlines, "l": links})
