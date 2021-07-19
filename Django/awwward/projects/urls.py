from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.welcome,name = 'welcome'),
    path('profile/',views.Profile,name = 'profile'),
    path('editprofile/',views.edit_Profile,name = 'editprofile'),
    path('projects/',views.project,name = 'projects'),
    path('newproject/',views.newProject,name = 'newProject'),
    # path('rate/<id>/',views.rate,name = 'rate')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
