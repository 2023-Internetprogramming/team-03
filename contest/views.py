from django.shortcuts import render
from .models import Contest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def contest_list(request):
    contests = Contest.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(contests, 8) 
    try:
        otts = paginator.page(page)
    except PageNotAnInteger:
        otts = paginator.page(1)
    except EmptyPage:
        otts = paginator.page(paginator.num_pages)

    return render(request, 'contest/contest_list.html', {'contests': contests, 'page_obj': contests})
