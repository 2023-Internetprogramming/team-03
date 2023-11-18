from django.urls import path
from .views import RideListView, RideDetailView, RideCreateView

urlpatterns = [
    path('rides/', RideListView.as_view(), name='ride_list'),
    path('rides/<int:pk>/', RideDetailView.as_view(), name='ride_detail'),
    path('rides/create/', RideCreateView.as_view(), name='ride_create'),
]