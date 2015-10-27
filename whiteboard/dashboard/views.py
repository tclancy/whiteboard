import pywapi

from django.shortcuts import render

# Create your views here.
def home(request):
    results = pywapi.get_weather_from_weather_com("03820", units="imperial")
    return render(request, "dashboard/index.html", {"forecasts": results.get("forecasts")})
