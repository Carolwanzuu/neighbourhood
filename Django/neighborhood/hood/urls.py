from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', include('hood.urls')),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
]