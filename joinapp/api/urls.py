from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('api/users', views.AllUsers, name="all_users" ),
    path('api/register/', views.Register, name="register" ),
    # path('api/login/', views.LoginData ),
    # path('api/register/add', views.RegisterUser ),
]