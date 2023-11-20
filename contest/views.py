from django.shortcuts import render
from .models import Contest, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect


def contest_list(request):
    contests = Contest.objects.order_by('-pk')
    
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
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.contest = contest
            comment.save()
    else:
        form = CommentForm()
    
    contest.contest_view_count += 1
    contest.save()
    
    return render(request, 'contest/contest_detail.html', {'contest': contest})