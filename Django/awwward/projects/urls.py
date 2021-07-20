from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('',views.welcome,name = 'welcome'),
    path('register/',views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/',views.Profile,name = 'profile'),
    path('editprofile/',views.edit_Profile,name = 'editprofile'),
    path('searchPro/', views.searchprofile, name='search'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('projects/',views.project,name = 'projects'),
    path('newproject/',views.newProject,name = 'newProject'),
    path('search/', views.search_project, name='search'),
    path('rate/<id>/',views.rate,name = 'rate')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
