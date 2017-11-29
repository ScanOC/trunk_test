from django.shortcuts import render

from django.views.generic import ListView

from trunk_web.models import Station

class StationList(ListView):
    model = Station
