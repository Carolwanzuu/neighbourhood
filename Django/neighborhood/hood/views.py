from .models import NeighborHood, Business,Profile, Post
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import NeighborHoodForm, SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def signup(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def hoods(request):
    all_hoods = NeighborHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'hoods.html', params)

def new_hood(request):
    if request.method == 'POST':
        form = NeighborHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighborHoodForm()
    return render(request, 'newhood.html', {'form': form})


def single_hood(request, hood_id):
    hood = NeighborHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single-hood', hood.id)
    else:
        form = BusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'single_hood.html', params)


def hood_members(request, hood_id):
    hood = NeighborHood.objects.get(id=hood_id)
    members = Profile.objects.filter(neighbourhood=hood)
    return render(request, 'members.html', {'members': members})


def create_post(request, hood_id):
    hood = NeighborHood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighborHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')


def leave_hood(request, id):
    hood = get_object_or_404(NeighborHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')


def profile(request):
    return render(request, 'profile.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': form})


def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, "results.html")