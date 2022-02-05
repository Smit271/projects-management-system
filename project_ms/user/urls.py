from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]