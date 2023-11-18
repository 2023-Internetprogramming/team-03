from django.shortcuts import render, redirect
from .models import Ride
from .forms import RideForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

def ride_list(request):
    rides = Ride.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(rides, 10) 
    try:
        rides = paginator.page(page)
    except PageNotAnInteger:
        rides = paginator.page(1)
    except EmptyPage:
        rides = paginator.page(paginator.num_pages)

    return render(request, 'taxi_posts/ride_list.html', {'rides': rides, 'page_obj': rides})

def ride_detail(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    return render(request, 'taxi_posts/ride_detail.html', {'ride': ride})

def ride_create(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return HttpResponseRedirect('/rides/')
    form = RideForm()
    return render(request, 'taxi_posts/ride_form.html', {'form': form})

# from django.contrib.auth.decorators import login_required
# @login_required
# def ride_create(request):
#     if request.method == 'POST':
#         form = RideForm(request.POST)
#         if form.is_valid():
#             new_item = form.save(commit=False)
#             new_item.user = request.user  # 현재 로그인한 사용자 설정
#             new_item.save()
#             return redirect('ride_list')  # 게시물이 성공적으로 저장되면 어떤 URL로 이동할지 설정
#     else:
#         form = RideForm()

#     return render(request, 'your_template.html', {'form': form})


def ride_delete(request):
    ride_id = request.GET.get('id')
    
    if ride_id:
        item = get_object_or_404(Ride, pk=ride_id)
        item.delete()
        
    return redirect('ride_list')

def ride_update(request, id):
    item = get_object_or_404(Ride, pk=id)

    if request.method == 'POST':
        form = RideForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('ride_detail', ride_id=item.id)

    else:
        form = RideForm(instance=item)

    return render(request, 'taxi_posts/ride_update.html', {'form': form})