from django.urls import path
from . import views

urlpatterns = [
    path('contest/', views.contest_list, name='contest_list'),
    path('contest/<int:contest_id>', views.contest_detail, name='contest_detail'),
]