from django.shortcuts import render, redirect
from .models import Ott
from .forms import OttForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

def ott_list(request):
    otts = Ott.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(otts, 8) 
    try:
        otts = paginator.page(page)
    except PageNotAnInteger:
        otts = paginator.page(1)
    except EmptyPage:
        otts = paginator.page(paginator.num_pages)

    return render(request, 'ott_posts/ott_list.html', {'otts': otts, 'page_obj': otts})

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


def ott_delete(request):
    ott_id = request.GET.get('id')
    
    if ott_id:
        item = get_object_or_404(Ott, pk=ott_id)
        item.delete()
        
    return redirect('ott_list')