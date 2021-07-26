from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>', views.profile, name='profile'),
    path('register/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('all_hoods/', views.hoods, name='hood'),
    path('new_hood/', views.new_hood, name='new_hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
]