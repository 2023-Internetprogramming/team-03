from django.urls import path
from . import views

urlpatterns = [
    path('rides/', views.ride_list, name='ride_list'),
    path('rides/<int:ride_id>/', views.ride_detail, name='ride_detail'),
    path('rides/new/', views.ride_create, name='ride_create'),
    path('rides_delete/', views.ride_delete, name='ride_delete'),
    path('rides_update/<int:id>/', views.ride_update, name='ride_update'),
    path('ride_search/', views.ridesearchResult, name='ridesearchResult'),
    path('<int:id>/ride_join/', views.ride_join, name="ride_join"),
    path('map/', views.map_view, name='map_view'),
    path('map2/', views.map2_view, name='map2_view'),
]