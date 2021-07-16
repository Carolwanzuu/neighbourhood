from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(blank=True, default='default.jpg')
    bio=models.TextField(max_length=255, default='My Bio',blank=True)
    name=models.CharField(max_length=50,blank=True)



