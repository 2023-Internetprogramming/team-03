from django.shortcuts import render
from .models import Contest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def contest_list(request):
    contests = Contest.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(contests, 8) 
    try:
        contests = paginator.page(page)
    except PageNotAnInteger:
        contests = paginator.page(1)
    except EmptyPage:
        contests = paginator.page(paginator.num_pages)

    return render(request, 'contest/contest_list.html', {'contests': contests, 'page_obj': contests})

def contest_detail(request, contest_id):
    contest = Contest.objects.get(id=contest_id)
    return render(request, 'contest/contest_detail.html', {'contest': contest})