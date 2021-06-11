from rest_framework import serializers

from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField

    # many is True as there can be many projects and internships for the same profile

    projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    internships = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('pk','stud_name','stud_id','desc','cgpa','email','password','projects','internships')


class ProjectSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    # many is set to false as a project can be related to only one profile
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(),many=False)     

    class Meta:
        model = Project
        fields = ('pk','profile','tags','title','desc','date_start','date_end','link')
        extra_kwargs = {'tags': {'required': False}}


class TagSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Tag
        fields = ("id", "tag_name", "projects")
        extra_kwargs = {'projects': {'required': False}}


class InternshipSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    # many is set to false as a project can be related to only one profile
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), many=False)

    class Meta:
        model = Internship
        fields = ('pk', 'profile', 'company','job_title', 'desc', 'date_start','date_end')
