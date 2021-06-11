from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer, ProjectSerializer, TagSerializer, InternshipSerializer
from .models import *


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Profile List': '/profile-list/',
        'Register':'/register-profile/',
        'Get Projects': '/project-list/<str:pk>/',
        'Get Internships':'/internship-list/<str:pk>/',
        'Get Tags': '/tag-list/',
        'Add Project':'/add-project/',
        'Add Internship':'/add-internship/',
        'Update Project': '/update-project/<str:pk>/',
        'Update Internship': '/update-internship/<str:pk>/',
        'Delete Project': '/delete-project/<str:pk>/',
        'Delete Internship': '/delete-internship/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def profileList(request):

    profiles = Profile.objects.all()

    serializer = ProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerProfile(request):
    serializer = ProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def projectList(request,pk):
    
    profile = Profile.objects.get(id=pk)

    projects = Project.objects.filter(profile=profile)

    serializer = ProjectSerializer(projects,many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def internshipList(request, pk):

    profile = Profile.objects.get(id=pk)

    internships = Internship.objects.filter(profile=profile)

    serializer = InternshipSerializer(internships, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def tagList(request):

    tags = Tag.objects.all()
    serializer = TagSerializer(tags,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addProject(request):

    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def addInternship(request):

    serializer = InternshipSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateProject(request,pk):

    project = Project.objects.get(id=pk)

    serializer = ProjectSerializer(instance=project, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateInternship(request, pk):

    internship = Internship.objects.get(id=pk)

    serializer = InternshipSerializer(instance=internship, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()

    return Response('Delete Successful!')


@api_view(['DELETE'])
def deleteInternship(request, pk):
    internship = Internship.objects.get(id=pk)
    internship.delete()

    return Response('Delete Successful!')
