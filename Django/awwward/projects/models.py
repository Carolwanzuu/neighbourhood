from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(blank=True, default='default.jpg')
    bio=models.TextField(max_length=255, default='My Bio',blank=True)
    name=models.CharField(max_length=50,blank=True)

class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    project_photo = models.ImageField(manual_crop='1280x720')
    projecturl= models.URLField(max_length=200)
    technologies=models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    datecreated= models.DateField(auto_now_add=True )



