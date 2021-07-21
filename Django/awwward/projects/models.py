from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
# from django.contrib.contenttypes.fields import GenericRelation
# from star_ratings.models import Rating

# Create your models here.
class Profiles(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic=models.ImageField(blank=True,null=True,upload_to = 'images/', default='default.png')
    bio=models.TextField(max_length=255, default='My Bio',blank=True)
    name=models.CharField(max_length=50,blank=True)
    contact=models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
 
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.ImageField(blank=True, null = True, upload_to = 'images/', default='images/default.png')
    projectUrl= models.URLField(max_length=200)
    technologies=models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(Profiles, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    datecreated= models.DateField(auto_now_add=True )

    def save_projects(self):
        self.user

    def delete_projects(self):
        self.delete()    


    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()

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

class Review(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    projects = models.ForeignKey(Projects,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    design = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default= 0)
    usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    content = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)

    def __str__(self):
        return self.user.username

# class Foo(models.Model):
#     bar = models.CharField(max_length=100)
#     ratings = GenericRelation(Rating, related_query_name='foos')

# Foo.objects.filter(ratings__isnull=False).order_by('ratings__average')
    



