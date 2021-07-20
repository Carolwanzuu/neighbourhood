from django import forms
from django.forms.fields import ImageField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profiles, Projects,Review,RATE_CHOICES


class profileForm(forms.ModelForm):
    class Meta:
        model = Profiles
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
        model = Profiles
        fields = ['bio', 'profilePic', 'contact']

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:

            user.save()
        return user

class RatingForm(forms.ModelForm):
   
    class Meta:
        model = Review
        fields = ['text','design','usability','content']
    