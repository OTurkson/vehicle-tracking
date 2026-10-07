from django.urls import path
from . import views

app_name = "vehicles"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_vehicle, name='create_vehicle'),
    path('<int:pk>/edit/', views.edit_vehicle, name='edit_vehicle'),
    path('<int:pk>/delete/', views.delete_vehicle, name='delete_vehicle'),
]