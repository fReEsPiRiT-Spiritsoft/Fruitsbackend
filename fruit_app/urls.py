from django.contrib import admin
from django.urls import path
from .views import send_fruits, info_view

urlpatterns = [
    path('', send_fruits, name='fruitlist'),
    path('info/', info_view, name='info')
]
