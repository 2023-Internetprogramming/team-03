from django.urls import path
from .views import ott_list, ott_detail, ott_create
from . import views

urlpatterns = [
    path('ott/', ott_list, name='ott_list'),
    path('ott/<int:ott_id>/', ott_detail, name='ott_detail'),
    path('ott/new/', ott_create, name='ott_create'),
    path('ott_delete/', views.ott_delete, name='ott_delete'),
]