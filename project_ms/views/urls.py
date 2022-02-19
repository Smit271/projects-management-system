from django.urls import path
from . import views
app_name = 'views'

urlpatterns = [
    # path('', views.index, name='index'),
    path('project-view/', views.project_view, name='project-view'),
    path('users-view/', views.users_view, name='users-view'),
]