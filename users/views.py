from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import logout

def main_view(request):
    return render(request, 'users/main_page.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"환영합니다, {user.username}님! 회원가입에 성공했습니다.")
            logout(request)  # 현재 사용자 로그아웃
            return render(request, 'users/signup.html', {'form': form, 'success_modal': True})
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
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main')