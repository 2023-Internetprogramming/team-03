from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('<int:study_id>/', views.study_detail, name='study_detail'),
    path('new/', views.study_create, name="study_create"),
    path('study_update/<int:id>/', views.study_update, name='study_update'),
    path('study_delete/', views.study_delete, name="study_delete"),
    path('study_search/', views.studysearchResult, name='studysearchResult'),

] 