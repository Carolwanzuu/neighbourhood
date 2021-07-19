from projects.forms import *
from .models import Projects
from django.shortcuts import redirect, render
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    projects = Projects.objects.all()
    return render(request, 'index.html',)

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=profileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()

            # messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
        prof=profileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'registration/register.html', params)

def Profiles(request):
    prof = Profile.objects.all()
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

def searchprofile(request):
    if 'searchUser' in request.GET and request.GET['searchUser']:
        name = request.GET.get("searchUser")
        searchResults = Projects.search_projects(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any profile"
    return render(request, 'search.html', {'message': message})
    

def project(request):
    proj = Projects.objects.all
    return render(render,'project.html')

@login_required(login_url='login')   
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
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Projects.objects.filter(title=title).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html')

@login_required(login_url='login')   
def rate(request,id):
    # reviews = Revieww.objects.get(projects_id = id).all()
    # print
    project = Projects.objects.get(id = id)
    user = request.user
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.projects = project
            rate.save()
            return redirect('home')
    else:
        form = RatingForm()
    return render(request,"rates.html",{"form":form,"project":project})        

def news_user(request):
    if request.method == 'POST':
        form = profileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = profileForm(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            
    return render(request, 'index.html')
