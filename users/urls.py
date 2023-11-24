from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.main_view, name='main'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('get_posts_by_category/', views.get_posts_by_category, name='get_posts_by_category'),
]