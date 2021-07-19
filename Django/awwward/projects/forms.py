from django import forms
from django.forms.fields import ImageField
from .models import Profile, Projects,Review,RATE_CHOICES


class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profilePic', 'Bio']

class projectForm(forms.ModelForm):
    photo = ImageField()
    
    class Meta:
        model = Projects
        fields = ['projectPhoto', 'title', 'projectUrl', 'description', 'technologies']
    