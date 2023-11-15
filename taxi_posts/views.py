from django.shortcuts import render, redirect
from .models import Ride
from .forms import RideForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def ride_list(request):
    rides = Ride.objects.all()
    return render(request, 'taxi_posts/ride_list.html', {'rides': rides})

def ride_detail(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    return render(request, 'taxi_posts/ride_detail.html', {'ride': ride})

def ride_create(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return HttpResponseRedirect('/rides/')
    form = RideForm()
    return render(request, 'taxi_posts/ride_form.html', {'form': form})
