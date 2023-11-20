from django.shortcuts import render, get_object_or_404, redirect
from .models import Study
from .forms import StudyForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def study_list(request):
    studys = Study.objects.all().order_by('-pk')

    page = request.GET.get('page', 1)
    paginator = Paginator(studys, 10)
    try:
        studys = paginator.page(page)
    except PageNotAnInteger:
        studys = paginator.page(1)
    except EmptyPage:
        studys = paginator.page(paginator.num_pages)

    return render(
        request,
        'study_posts/study_list.html',
        {
            'studys' : studys,
            'page_obj': studys,
        }
    )

def study_detail(request, study_id):
    study = Study.objects.get(pk=study_id)

    return render(
        request,
        'study_posts/study_detail.html',
        {
            'study' : study
        }
    )

def study_create(request):
    if request.method == 'POST': 
        form = StudyForm(request.POST)   
        if form.is_valid():
            new_item = form.save()
            return redirect('/study/')

    form = StudyForm()
    return render(request, 'study_posts/study_form.html', {'form': form})

def study_delete(request):
    study_id = request.GET.get('id')
    
    if study_id:
        item = get_object_or_404(Study, pk=study_id)
        item.delete()
    
    return redirect('/study/')

def study_update(request, id):
    item = get_object_or_404(Study, pk=id)

    if request.method == "POST":
        form = StudyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('study_detail', study_id=item.id)
    else:
        form = StudyForm(instance=item)
    
    return render(request, "study_posts/study_edit.html", {'form': form})
