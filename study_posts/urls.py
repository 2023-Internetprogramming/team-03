from django.urls import path
from . import views

urlpatterns = [
    path('', views.studyList),
    path('<int:pk>/', views.studyDetail),
    path('create_study/', views.studyCreate, name="create_study"),
    path('<int:pk>/update/', views.studyUpdate, name='update_study'),
    path('<int:pk>/delete/', views.studyDelete, name="delete_study"),

] 