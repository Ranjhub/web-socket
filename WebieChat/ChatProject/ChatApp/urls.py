# chat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('chat/<str:room_name>/', views.room, name='room'),
]
