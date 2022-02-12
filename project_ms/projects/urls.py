from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('/', views.projects, name='projects'),
    path('create-project/', views.Project, name='create-project'),
    path('create-task/', views.Task, name='create-task'),
]