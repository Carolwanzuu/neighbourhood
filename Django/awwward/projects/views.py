from projects.forms import *
from .models import Projects
from django.shortcuts import redirect, render

# Create your views here.
def welcome(request):
    projects = Projects.objects.all()
    return render(request, 'index.html',)

def register(request):
    return render(request, 'users/register.html')

def Profiles(request):
    prof = Profile.objects.get(user = id)
    return render(request, 'profile.html')

def edit_Profile(request):
    user= request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile', user.id)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UpdateProfileForm()
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'editProfile.html', context)
    

def project(request):
    proj = Projects.objects.all
    return render(render,'project.html')

def newProject(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid:
            newProj = form.save(commit = False)
            newProj.user = user_profile
            newProj.save()
        return redirect('home')  
    else:
        form = projectForm()
    return render(request,'newProj.html',{'form':form})    

def search_project(request):
    return render(request, 'results.html')

