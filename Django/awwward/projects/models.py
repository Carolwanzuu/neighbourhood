from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(blank=True, default='default.jpg')
    bio=models.TextField(max_length=255, default='My Bio',blank=True)
    name=models.CharField(max_length=50,blank=True)
    contact=models.EmailField(max_length=100, blank=True)

class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    project_photo = models.ImageField(blank=True)
    projecturl= models.URLField(max_length=200)
    technologies=models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    datecreated= models.DateField(auto_now_add=True )

RATE_CHOICES = [
(1,'1- Trash'),
(2,'2- Horrible'),
(3,'3- Terrible'),
(4,'4- Bad'),
(5,'5- Ok'),
(6,'6- Watchable'),
(7,'7- Good'),
(8,'8- Very Good'),
(9,'9- perfect'),
(10,'10- Master Piece'),
]

class Revieww(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    projects = models.ForeignKey(Projects,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    design = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default= 0)
    usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    content = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    



