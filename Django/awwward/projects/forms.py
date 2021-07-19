from django import forms
from django.forms.fields import ImageField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Projects,Review,RATE_CHOICES


class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profilePic', 'bio']

class projectForm(forms.ModelForm):
    photo = ImageField()
    
    class Meta:
        model = Projects
        fields = ['photo', 'title', 'projectUrl', 'description', 'technologies']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email'] 

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profilePic', 'contact']
    