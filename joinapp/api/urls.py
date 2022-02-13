from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegistertData ),
    path('login/', views.LoginData ),
]