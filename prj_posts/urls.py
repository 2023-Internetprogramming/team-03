from django.urls import path
from . import views

urlpatterns = [
    path('', views.prjList),
    path('<int:pk>/', views.prjDetail),
    path('create_prj/', views.prjCreate, name="create_prj"),
    path('<int:pk>/update/', views.prjUpdate, name='update_prj'),
    path('<int:pk>/delete/', views.prjDelete, name="delete_prj"),
] 