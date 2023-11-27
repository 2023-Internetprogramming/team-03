from django.urls import path
from . import views

urlpatterns = [
    path('ott/', views.ott_list, name='ott_list'),
    path('ott/<int:ott_id>/', views.ott_detail, name='ott_detail'),
    path('ott/new/', views.ott_create, name='ott_create'),
    path('ott_delete/', views.ott_delete, name='ott_delete'),
    path('ott_update/<int:id>/', views.ott_update, name='ott_update'),
    path('ott_search/', views.ottsearchResult, name='ottsearchResult'),
]