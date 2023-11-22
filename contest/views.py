from django.shortcuts import render
from .models import Contest, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime, timedelta



def contest_list(request):
    contests = Contest.objects.order_by('-pk')
    today = datetime.now().date()
    
    for contest in contests:
        contest.deadline = (contest.deadline - today).days
    
    page = request.GET.get('page', 1)
    paginator = Paginator(contests, 8) 
    try:
        contests = paginator.page(page)
    except PageNotAnInteger:
        contests = paginator.page(1)
    except EmptyPage:
        contests = paginator.page(paginator.num_pages)

    return render(request, 'contest/contest_list.html', {'contests': contests, 'page_obj': contests})

# def contest_detail(request, contest_id):
    # contest = get_object_or_404(Contest, id=contest_id)
    # comments = Comment.objects.filter(contest=contest)

    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.user = request.user
    #         comment.contest = contest
    #         comment.save()
    #         return redirect('contest_detail', contest_id=contest.id)
    # else:
    #     form = CommentForm()

    # return render(request, 'contest_detail.html', {'contest': contest, 'comments': comments, 'form': form})
    
    
def contest_detail(request, contest_id):
    contest = Contest.objects.get(id=contest_id)
    
    contest.contest_view_count += 1
    contest.save()

    # Add the contest_id to the viewed_contests list in the session
    request.session['viewed_contests'].append(contest_id)
    request.session.modified = True
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.contest = contest
            comment.save()
    else:
        form = CommentForm()
    
    return render(request, 'contest/contest_detail.html', {'contest': contest})


@require_POST
@login_required
def scrap_contest(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)

    # 사용자가 이미 해당 콘테스트를 스크랩한 경우 중복을 피하기 위해 체크
    if request.user in contest.scraped_by_users.all():
        return JsonResponse({'status': 'error', 'message': '이미 스크랩한 공모전입니다'})

    # 현재 사용자를 스크랩한 사용자 목록에 추가
    contest.scraped_by_users.add(request.user)

    return JsonResponse({'status': 'success', 'message': '공모전이 스크랩되었습니다'})