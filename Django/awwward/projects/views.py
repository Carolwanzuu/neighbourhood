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
    user= request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.id)
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'editprofile.html', params)
    return render(request,'editProfile.html')

def project(request):
    return render(render,'project.html')

def search_project(request):
    return render(request, 'results.html')

