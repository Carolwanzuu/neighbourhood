from rest_framework import serializers
from .models import Profiles,Projects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('Bio', 'profilePic', 'user')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'photo','projectUrl','user')