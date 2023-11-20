
from django.shortcuts import render, get_object_or_404, redirect
from .models import Prj
from .forms import PrjForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def prj_list(request):
    prjs = Prj.objects.all().order_by('-pk')

    page = request.GET.get('page', '1')
    paginator = Paginator(prjs, 10)
    
    try:
        prjs = paginator.page(page)
    except PageNotAnInteger:
        prjs = paginator.page(1)
    except EmptyPage:
        prjs = paginator.page(paginator.num_pages)    

    return render(
        request,
        'prj_posts/prj_list.html',
        {
            'rides': prjs, 
            'page_obj': prjs        
        },
    )

def prj_detail(request, prj_id):
    prj = Prj.objects.get(id=prj_id)
    return render(request, 'prj_posts/prj_form.html', {'prj': prj})

def prj_create(request):
    if request.method == 'POST':
        form = PrjForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return HttpResponseRedirect('/prjs/')
    form = PrjForm()
    return render(request, 'prj_posts/prj_form.html', {'form': form})

def prj_delete(request):
    prj_id = request.GET.get('id')
    
    if prj_id:
        item = get_object_or_404(Prj, pk=prj_id)
        item.delete()
        
    return redirect('prj_list')

def prj_update(request, id):
    item = get_object_or_404(Prj, pk=id)

    if request.method == "POST":
        form = PrjForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('prj_detail', prj_id=item.id)
    else:
        form = PrjForm(instance=item)

    return render(request, "prj_posts/prj_edit.html", {'form': form})