from django.urls import path
from .views import OttListView, OttDetailView, OttCreateView

urlpatterns = [
    path('ott/', OttListView.as_view(), name='ott_list'),
    path('ott/<int:pk>/', OttDetailView.as_view(), name='ott_detail'),
    path('ott/new/', OttCreateView.as_view(), name='ott_create'),
]