import datetime
import json
import urllib
from django.shortcuts import render
from forecast.forms import ForecastForm

COORDS = [
    (),
    (50.581118, 16.659904),  # Srebrna Góra
    (50.25747112249451, 16.823442505499724),  # Czarna Góra
    (50.30182059820614, 17.15883468814209),  # Rychleby
    (50.09927389797321, 17.120427569944297),  # Kouty
    (49.779281051488084, 19.0553671754885),  # Bielsko-Białą

]


def forecast_view(request):

    if request.method == 'POST':
        form = ForecastForm(request.POST)
        if form.is_valid():
            i = int(form.cleaned_data['location'])
            with open("appid.txt") as f:
                appid = f.read().strip()
            url = f'https://api.openweathermap.org/data/2.5/forecast?lat={COORDS[i][0]}&lon={COORDS[i][1]}&appid={appid}'
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            for d in data["list"]:
                value = d["dt"]
                d["dt"] = datetime.datetime.fromtimestamp(int(value))
            form = ForecastForm()
            return render(request, "forecast/forecast_lookup.html", {'data': data, 'form': form})

    else:
        form = ForecastForm()

    return render(request, 'forecast/forecast.html', {'form': form})
