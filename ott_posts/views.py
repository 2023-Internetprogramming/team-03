from django.shortcuts import render, redirect
from .models import Ott
from .forms import OttForm
from django.http import HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def ott_list(request):
    otts = Ott.objects.order_by('-pk')

    page_number = request.GET.get('page', 1)
    paginator = Paginator(otts, 10)

    try:
        otts = paginator.page(page_number)
    except PageNotAnInteger:
        otts = paginator.page(1)
    except EmptyPage:
        otts = paginator.page(paginator.num_pages)

    return render(request, 'ott_posts/ott_list.html', {'otts': otts, 'page_obj': otts})


def ott_detail(request, ott_id):
    ott = get_object_or_404(Ott, id=ott_id)
    room_name_json = f'/chat/ott{ott_id}/'
    return render(request, 'ott_posts/ott_detail.html', {'ott': ott, 'room_name_json': room_name_json})


@login_required
def ott_create(request):
    if request.method == 'POST':
        form = OttForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.author = request.user  # 사용자 정보를 글과 연결
            new_item.save()
            return HttpResponseRedirect('/ott/')
    form = OttForm()
    return render(request, 'ott_posts/ott_form.html', {'form': form})


@login_required
def ott_delete(request):
    ott_id = request.GET.get('id')

    if ott_id:
        item = get_object_or_404(Ott, pk=ott_id)

        # 사용자가 글의 작성자인지 확인
        if request.user != item.author:
            return HttpResponseForbidden("글을 삭제할 권한이 없습니다.")
        
        item.delete()
        
    return redirect('ott_list')


@login_required
def ott_update(request, id):
    item = get_object_or_404(Ott, pk=id)

    if request.user != item.author:
        return HttpResponseForbidden("글을 수정할 권한이 없습니다.")
    
    if request.method == 'POST':
        form = OttForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('ott_detail', ott_id=item.id)

    else:
        form = OttForm(instance=item)

    return render(request, 'ott_posts/ott_update.html', {'form': form})


#검색
def ottsearchResult(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        otts = Ott.objects.filter(
            Q(type__icontains=query) |
            Q(people__icontains=query) |
            Q(bill__icontains=query) |
            Q(description_OTT__icontains=query)
        )
        return render(request, 'ott_posts/ott_search.html', {'query': query, 'otts': otts})
    else:
        return render(request, 'ott_posts/ott_search.html')

@login_required
def ott_join(request, id):
    item = get_object_or_404(Ott, pk=id)

    esisted_user = item.join_list.filter(pk=request.user.id).exists()
    
    if (request.user == item.author or esisted_user):
        return JsonResponse({'success': True})

    else:
        if (item.people > 0):
            item.join_list.add(request.user)
            item.people -= 1
            item.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})