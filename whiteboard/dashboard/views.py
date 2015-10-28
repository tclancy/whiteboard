import pywapi

from django.conf import settings
from django.shortcuts import render

from dashboard.events import get_events

# Create your views here.
def home(request):
    """
    Initial view of things, break all this crap out into testable functions in another file
    """
    results = pywapi.get_weather_from_weather_com("03820", units="imperial")
    return render(request, "dashboard/index.html", {
        "forecasts": results.get("forecasts"),
        "events": get_events()
    })
