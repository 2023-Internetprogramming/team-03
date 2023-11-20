from django.shortcuts import render, get_object_or_404, redirect
from .models import Study
from .forms import StudyForm
from datetime import datetime


def studyList(request):
    studys = Study.objects.all().order_by('-pk')

    return render(
        request,
        'study_posts/study_list.html',
        {
            'studys' : studys,
        }
    )

def studyDetail(request, pk):
    study = Study.objects.get(pk=pk)

    return render(
        request,
        'study_posts/study_detail.html',
        {
            'study' : study
        }
    )

def studyCreate(request):
    if request.method == 'POST': 
        form = StudyForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('/study/')

    else:
        form = StudyForm()
        return render(request, 'study_posts/study_form.html', {'form': form})
    

def studyUpdate(request, pk):
    study = Study.objects.get(pk=pk)
    if request.method == "POST":
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            prj = form.save(commit = False)
            prj.save()
            return redirect('/study/'+str(pk))
    else:
        form = StudyForm(instance=study)
        return render(request, "study_posts/study_edit.html", {'form': form})


def studyDelete(request, pk):
    study = Study.objects.get(pk=pk)
    # if study.writer == request.user or request.user.level == '0': # 작성자 확인
    study.delete()
    return redirect('/study/')
    # else:
    #     return redirect('/notice/'+str(pk)) 
