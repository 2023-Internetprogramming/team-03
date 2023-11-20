
from django.shortcuts import render, get_object_or_404, redirect
from .models import Prj
from .forms import PrjForm
from django.core.paginator import Paginator  


def prjList(request):
    prjs = Prj.objects.all().order_by('-pk')

    page = request.GET.get('page', '1')
    paginator = Paginator(prjs, 10)
    
    page_obj = paginator.get_page(page)
    
    return render(
        request,
        'prj_posts/prj_list.html',
        {
            'prjList': page_obj,
        },
    )

def prjDetail(request, pk):
    prj = Prj.objects.get(pk=pk)

    return render(
        request,
        'prj_posts/prj_detail.html',
        {
            'prj' : prj
        }
    )

def prjCreate(request):
    if request.method == 'POST': 
        form = PrjForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('/prj/')

    else:
        form = PrjForm()
        return render(request, 'prj_posts/prj_form.html', {'form': form})

def prjUpdate(request, pk):
    prj = Prj.objects.get(pk=pk)
    if request.method == "POST":
        form = PrjForm(request.POST, instance=prj)
        if form.is_valid():
            prj = form.save(commit = False)
            prj.save()
            return redirect('/prj/'+str(pk))
    else:
        form = PrjForm(instance=prj)
        return render(request, "prj_posts/prj_edit.html", {'form': form})


def prjDelete(request, pk):
    prj = Prj.objects.get(pk=pk)
    # if prj.writer == request.user or request.user.level == '0': # 작성자 확인
    prj.delete()
    return redirect('/prj/')
    # else:
    #     return redirect('/notice/'+str(pk)) 
