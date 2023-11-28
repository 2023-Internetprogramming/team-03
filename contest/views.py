from django.shortcuts import render
from .models import Contest, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Count




def contest_list(request):
    category_filter = request.GET.get('category', None)
    if category_filter:
        contests = Contest.objects.filter(contest_category=category_filter).order_by('-pk')
    else:
        contests = Contest.objects.order_by('-pk')


    for contest in contests:
        contests = contests.annotate(comments_count=Count('comment'))

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
    
    contest.contest_view_count += 1
    contest.save()

    # Initialize or retrieve the 'viewed_contests' list in the session
    viewed_contests = request.session.get('viewed_contests', [])
    
    # Add the contest_id to the 'viewed_contests' list in the session if not already present
    if contest_id not in viewed_contests:
        viewed_contests.append(contest_id)
        request.session['viewed_contests'] = viewed_contests
        request.session.modified = True
        
    comments_count = Comment.objects.filter(contest_post=contest).count()
    
    return render(request, 'contest/contest_detail.html', {'contest': contest, 'comments_count': comments_count})


@require_POST
@login_required
def scrap_contest(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)

    # 사용자가 이미 해당 콘테스트를 스크랩한 경우
    if request.user in contest.scraped_by_users.all():
        # 스크랩 취소
        contest.scraped_by_users.remove(request.user)
        message = '공모전 스크랩이 취소되었습니다.'
    else:
        # 스크랩
        contest.scraped_by_users.add(request.user)
        message = '공모전이 스크랩되었습니다.'

    return JsonResponse({'status': 'success', 'message': message})


def comment(request, contest_id):
    contest = Contest.objects.get(id=contest_id)
    comments = Comment.objects.filter(contest_post=contest).order_by('-created_at')  # 작성 시간에 따라 내림차순 정렬
    comments_count = comments.count()  # 댓글 수를 미리 계산

    if request.method == "POST":
        comment_text = request.POST.get('comment', '')
        if comment_text:
            comment = Comment()
            comment.comment = comment_text
            comment.author = request.user
            comment.contest_post = contest
            comment.save()

            # 댓글이 추가된 후에 새로고침 시 새 댓글이 맨 위에 보이도록 함
            comments = Comment.objects.filter(contest_post=contest).order_by('-created_at')
            comments_count = comments.count()

    return render(request, 'contest/comment.html', {'comments': comments, 'contest': contest, 'comments_count': comments_count})


@require_POST
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the logged-in user is the author of the comment
    if request.user == comment.author:
        comment.delete()
        message = '댓글이 삭제되었습니다.'
    else:
        message = '댓글을 삭제할 권한이 없습니다.'

    return JsonResponse({'status': 'success', 'message': message})



#검색
def searchResult(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        contests = Contest.objects.filter(
            Q(contest_title__icontains=query) |
            Q(contest_description__icontains=query) |
            Q(contest_category__icontains=query)
        )
        return render(request, 'contest/contest_search.html', {'query': query, 'contests': contests})
    else:
        return render(request, 'contest/contest_search.html')