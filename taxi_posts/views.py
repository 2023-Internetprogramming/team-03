from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Ride
from .forms import RideForm
from django.urls import reverse_lazy

class RideListView(ListView):
    model = Ride
    template_name = 'taxi_posts/ride_list.html'
    context_object_name = 'rides'
    paginate_by = 10
    
    def get_queryset(self):
        return Ride.objects.all().order_by('-departure_time')

class RideDetailView(DetailView):
    model = Ride
    template_name = 'taxi_posts/ride_detail.html'
    context_object_name = 'ride'

class RideCreateView(CreateView):
    model = Ride
    form_class = RideForm
    template_name = 'taxi_posts/ride_form.html'
    success_url = reverse_lazy('ride_list')
