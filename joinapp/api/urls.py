from django import views
from django.urls import path
from . import views


urlpatterns = [
    #path('api/', views.edxUserApi, name="api" ),
    path('api/register/', views.Register, name="register" ),
    # path('api/login/', views.LoginData ),
    # path('api/register/add', views.RegisterUser ),
]