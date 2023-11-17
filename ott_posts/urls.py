from django.urls import path
from .views import ott_list, ott_detail, ott_create

urlpatterns = [
    path('ott/', ott_list, name='ott_list'),
    path('ott/<int:ott_id>/', ott_detail, name='ott_detail'),
    path('ott/new/', ott_create, name='ott_create'),
]