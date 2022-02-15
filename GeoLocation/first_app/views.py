from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import *

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from .utils import get_geo

import requests
import json


# Create your views here.

def index(request):
    obj = get_object_or_404(Mesurment, id=5)
    form = MesurmentForm()
    geolocator = Nominatim(user_agent="first_app")
    form = MesurmentForm(request.POST)
    ip = '72.14.207.99'
    country, city, lat,lon = get_geo(ip)
    location =  geolocator.geocode(city)
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)
    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)
        distance = round(geodesic(pointA, pointB).km, 2)
        instance.location = location
        instance.distance = distance
        instance.save()
        return HttpResponse('ok')
    context = {
        'obj': obj,
        'form': form,
    }
    return render(request, 'index.html', context)

#user locaiton
def locator(request):
    ip = request.META.get('REMOTE_ADDR')
    ip = request.session['ip']=ip
    print("===================",ip)
    # ip = request.session.get('ip', 1234567890)
    res = requests.get('http://ip-api.com/json/'+ip)
    location = res.text
    location_data = json.loads(location)
    context = {'data': location_data, 'ip':ip}
    return render(request, 'location.html', context)



#get ip
def get_user_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    ip = request.session['ip']=ip
    context = {'ip':ip}
    return render(request, 'get_user_ip.html', context)



def user_form(request):
    user_f = UserForm.objects.all()
    print("====================", user_f)
    context = {'user_f': user_f,}
    return render(request, 'user_form.html', context)

























#
#
# import ipinfo_django
# import request
# def location(request):
#     response_string = 'The IP address {} is located at the coordinates {}, which is in the city {}.'.format(
#         request.ipinfo.ip,
#         request.ipinfo.loc,
#         request.ipinfo.city
#     )
#     return HttpResponse(response_string)
