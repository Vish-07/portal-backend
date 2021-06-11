
from django.urls import path
from . import views


urlpatterns=[
    path('',views.apiOverview,name="api-overview"),
    path('profile-list/',views.profileList,name="profile-list"),
    path('register-profile/', views.registerProfile,name="register-profile"),
    path('project-list/<str:pk>/', views.projectList, name="project-list"),
    path('internship-list/<str:pk>/', views.internshipList, name="internship-list"),
    path('add-project/', views.addProject, name="add-project"),
    path('add-internship/', views.addInternship, name="add-internship"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    path('update-internship/<str:pk>/',views.updateInternship, name="update-internship"),
    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
    path('delete-internship/<str:pk>/', views.deleteInternship, name="delete-internship"),
    path('tag-list/',views.tagList,name="tag-list"),

]
