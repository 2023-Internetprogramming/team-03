from django.urls import path
from . import views

urlpatterns = [
    path('contest/', views.contest_list, name='contest_list'),
]