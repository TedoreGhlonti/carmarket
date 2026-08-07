#cars urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('new/', views.car_create, name='car_create'),
    path('<int:pk>/', views.car_detail, name='car_detail'),
]