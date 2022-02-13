from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('api/register/', views.RegistertData ),
    path('api/login/', views.LoginData ),
    path('api/register/add', views.RegisterUser ),
]