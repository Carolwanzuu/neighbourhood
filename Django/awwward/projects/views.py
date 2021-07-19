from .models import Projects
from django.shortcuts import render

# Create your views here.
def welcome(request):
    projects = Projects.objects.all()
    return render(request, 'index.html',)

def register(request):
    return render(request, 'users/register.html')

def Profile(request):
    
    return render(request, 'profile.html')

def edit_Profile(request):
    return render(request,'editProfile.html')

def project(request):
    return render(render,'project.html')

def search_project(request):
    return render(request, 'results.html')

