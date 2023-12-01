from django.shortcuts import render, get_object_or_404, redirect
from .models import Study
from .forms import StudyForm
from django.http import HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def study_list(request):
    studys = Study.objects.all().order_by('-pk')

    page = request.GET.get('page', 1)
    paginator = Paginator(studys, 10)

    room_name_json = f'/chat/study'    

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
            'room_name_json': room_name_json
        }
    )


def study_detail(request, study_id):
    study = Study.objects.get(pk=study_id)

    return render(
        request,
        'study_posts/study_detail.html',
        {
            'study' : study,
        }
    )


@login_required
def study_create(request):
    if request.method == 'POST': 
        form = StudyForm(request.POST)   
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.author = request.user  # 사용자 정보를 글과 연결
            new_item.save()
            return redirect('/study/')

    form = StudyForm()
    return render(request, 'study_posts/study_form.html', {'form': form})


@login_required
def study_delete(request):
    study_id = request.GET.get('id')
    
    if study_id:
        item = get_object_or_404(Study, pk=study_id)
        
        if request.user != item.author:
            return HttpResponseForbidden("글을 삭제할 권한이 없습니다.")
        item.delete()
    
    return redirect('/study/')


@login_required
def study_update(request, id):
    item = get_object_or_404(Study, pk=id)
    
    if request.user != item.author:
        return HttpResponseForbidden("글을 수정할 권한이 없습니다.")

    if request.method == "POST":
        form = StudyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('study_list')
        # 모달창으로 돌아가지는게 안되서 일단 list페이지로 넘어가게 함
    else:
        form = StudyForm(instance=item)
    
    return render(request, "study_posts/study_update.html", {'form': form})


#검색
def studysearchResult(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        studys = Study.objects.filter(
            Q(post_title__icontains=query) |
            Q(user_name__icontains=query) |
            Q(user_major__icontains=query) |
            Q(user_grade__icontains=query) |
            Q(study_type__icontains=query) |
            Q(study_member__icontains=query) |
            Q(post_content__icontains=query)
        ).order_by('-created_at')
        return render(request, 'study_posts/study_search.html', {'query': query, 'studys': studys})
    else:
        return render(request, 'study_posts/study_search.html')
    
@login_required
def study_join(request, id):
    item = get_object_or_404(Study, pk=id)

    esisted_user = item.join_list.filter(pk=request.user.id).exists()
    
    if (request.user == item.author or esisted_user):
        return JsonResponse({'success': True})

    else:
        if (item.study_member > 0):
            item.join_list.add(request.user)
            item.study_member -= 1
            item.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})