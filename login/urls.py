from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.homePage, name='home'),
    path('logout/', views.logoutUser, name='logout'),
]