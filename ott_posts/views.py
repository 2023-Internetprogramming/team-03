from django.shortcuts import render, redirect
from .models import Ott
from .forms import OttForm
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

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
    ott = Ott.objects.get(id=ott_id)
    return render(request, 'ott_posts/ott_detail.html', {'ott': ott})

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

