from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='project'),
    path('create-project/', views.CreateProject, name='create-project'),
    path('create-task/', views.CreateTask, name='create-task'),
    path('project-detail/<int:id>/', views.ProjectDetail, name='project-detail'),
    path('update-project/<int:id>/', views.UpdateProject, name='update-project'),
    path('update-task/<int:id>/', views.UpdateTask, name='update-task'),
]