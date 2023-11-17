from django.shortcuts import render, redirect
from .models import Ott
from .forms import OttForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def ott_list(request):
    otts = Ott.objects.all()
    return render(request, 'ott_posts/ott_list.html', {'otts': otts})

def ott_detail(request, ott_id):
    ott = Ott.objects.get(id=ott_id)
    return render(request, 'ott_posts/ott_detail.html', {'ott': ott})

def ott_create(request):
    if request.method == 'POST':
        form = OttForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return HttpResponseRedirect('/ott/')
    form = OttForm()
    return render(request, 'ott_posts/ott_form.html', {'form': form})
