from django.urls import path
from forecast.views import forecast_view

urlpatterns = [
    path("", forecast_view, name='forecast')
]
