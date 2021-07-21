from _typeshed import Self
from django.test import TestCase
from pyuploadcare.dj.models import ImageField
from .models import Profiles,Projects
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.wanzuu = User(username = 'wanzuu',email = 'wanzuu@gmail.com')
        self.wanzuu = Profiles(user = Self.wanzuu,user = 1,Bio = 'tests',photo = 'test.jpg',date_craeted='July,20.2021')

    def test_instance(self):
        self.assertTrue(isinstance(self.wanzuu,Profiles))


    def test_save_profile(self):
        Profiles.save_profile(self)
        all_profiles = Profiles.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.wanzuu.delete_profile()
        all_profiles = Profiles.objects.all()
        self.assertEqual(len(all_profiles),0)



class ProjectsTestCase(TestCase):
    def setUp(self):
        self.new_post = Projects(title = 'testT',photo = 'test.jpg',description = 'testD',user ='favian',projectUrl = 'https://test.com',datecreated='July,20,2021')


    def test_save_project(self):
        self.new_post.save_project()
        pictures = ImageField.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        pictures = Projects.objects.all()
        self.assertEqual(len(pictures),1)    

   





