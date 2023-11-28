from django.shortcuts import render, redirect
from .models import Ride
from .forms import RideForm
from django.http import HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse


def ride_list(request):
    rides = Ride.objects.order_by('-pk')
    
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
    room_name_json = f'/chat/ride{ride_id}/'
    return render(request, 'taxi_posts/ride_detail.html', {'ride': ride, 'room_name_json': room_name_json})


@login_required
def ride_create(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.author = request.user
            new_item.save()
            return HttpResponseRedirect('/rides/')  # 변경된 부분
    else:
        form = RideForm()
    return render(request, 'taxi_posts/ride_form.html', {'form': form})



@login_required
def ride_delete(request):
    ride_id = request.GET.get('id')
    
    if ride_id:
        item = get_object_or_404(Ride, pk=ride_id)
        
        if request.user != item.author:
            return HttpResponseForbidden("글을 삭제할 권한이 없습니다.")
        
        item.delete()
        
    return redirect('ride_list')


@login_required
def ride_update(request, id):
    item = get_object_or_404(Ride, pk=id)
    
    if request.user != item.author:
        return HttpResponseForbidden("글을 수정할 권한이 없습니다.")

    if request.method == 'POST':
        form = RideForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('ride_detail', ride_id=item.id)

    else:
        form = RideForm(instance=item)

    return render(request, 'taxi_posts/ride_update.html', {'form': form})


#검색
def ridesearchResult(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        rides = Ride.objects.filter(
            Q(departure_location__icontains=query) |
            Q(destination__icontains=query) |
            Q(departure_time__icontains=query) |
            Q(available_seats__icontains=query) |
            Q(description__icontains=query) 
        )
        return render(request, 'taxi_posts/ride_search.html', {'query': query, 'rides': rides})
    else:
        return render(request, 'taxi_posts/ride_search.html')
    
@login_required
def ride_join(request, id):
    item = get_object_or_404(Ride, pk=id)

    esisted_user = item.join_list.filter(pk=request.user.id).exists()
    
    if (request.user == item.author or esisted_user):
        return JsonResponse({'success': True})

    else:
        if (item.available_seats > 0):
            item.join_list.add(request.user)
            item.available_seats -= 1
            item.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})    

def map_view(request):
    destination_title = request.GET.get('title', '')
    return render(request, 'taxi_posts/map.html', {'destination_title': destination_title})


def map2_view(request):
    destination_title = request.GET.get('title', '')
    return render(request, 'taxi_posts/map2.html', {'destination_title': destination_title})
