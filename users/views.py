from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from ott_posts.models import Ott
from prj_posts.models import Prj
from study_posts.models import Study
from taxi_posts.models import Ride
from contest.models import Contest
from .forms import EditProfileForm
from .models import UserProfile


def main_view(request):
    Prj_data = Prj.objects.all()
    Ride_data = Ride.objects.all()
    Ott_data = Ott.objects.all()
    Study_data = Study.objects.all()
    Contest_data = Contest.objects.all()
    return render(request, 'users/main_page.html', {'Prj_data': Prj_data, 'Ride_data': Ride_data, 'Ott_data': Ott_data, 'Study_data': Study_data, 'Contest_data': Contest_data})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            UserProfile.objects.create(
                user=user,
                phone_number=form.cleaned_data['phone_number'],
                real_name=form.cleaned_data['real_name']
            )
            
            logout(request)  # 현재 사용자 로그아웃
            return render(request, 'users/signup.html', {'form': form, 'success_modal': True, 'user_profile': user.userprofile})
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = form.get_user()
            login(request, user)
            
            return redirect('main')
        else:
            messages.error(request, '유효하지 않은 ID 또는 비밀번호입니다. 다시 시도해주세요.')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main')


@login_required
def mypage_view(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None 
    #스크랩
    saved_posts = user.scraped_contests.all()
    today = datetime.now().date()
    
    for contest in saved_posts:
        contest.deadline = contest.deadline - datetime.now().date()
        
    #자신이 작성한 글 
    ott_posts = Ott.objects.filter(author=user)
    prj_posts = Prj.objects.filter(author=user)
    study_posts = Study.objects.filter(author=user)
    taxi_posts = Ride.objects.filter(author=user)
    

    return render(request, 'users/mypage.html', {'saved_posts': saved_posts, 'ott_posts': ott_posts, 'prj_posts': prj_posts, 'study_posts': study_posts, 'taxi_posts': taxi_posts, 'user_profile': user_profile})


@login_required
def editmypage_view(request):
    user = request.user
    
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "프로필이 성공적으로 업데이트되었습니다.")
            return redirect('mypage')
        else:
            messages.error(request, "프로필 업데이트에 실패했습니다.")
    else:
        profile_form = EditProfileForm(instance=request.user.userprofile)

    return render(request, 'users/edit.html', {'profile_form': profile_form})