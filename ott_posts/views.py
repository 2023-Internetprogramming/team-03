from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Ott
from .forms import OttForm

class OttListView(ListView):
    model = Ott
    template_name = 'ott_posts/ott_list.html'
    context_object_name = 'otts'
    paginate_by = 10
    
    def get_queryset(self):
        return Ott.objects.all().order_by()

class OttDetailView(DetailView):
    model = Ott
    template_name = 'ott_posts/ott_detail.html'
    context_object_name = 'ott'

class OttCreateView(CreateView):
    model = Ott
    form_class = OttForm
    template_name = 'ott_posts/ott_form.html'
    success_url = '/ott/'

    def form_valid(self, form):
        return super().form_valid(form)