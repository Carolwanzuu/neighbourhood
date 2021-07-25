from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('register/', views.signup, name='signup'),
    # path('accounts/', include('django.contrib.auth.urls')),
]