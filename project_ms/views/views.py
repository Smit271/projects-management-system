from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from projects.models import Project, Task
from user.models import User

# Create your views here.
# def index(request):
#     print("Views index")
#     return render(request, 'views/index.html')


def project_view(request):
    print("Views Project")
    projects = Project.objects.all().order_by("id")
    # print(projects)

    context = {
        'projects' : projects,
    }
    return render(request, "views/index.html", context)


def users_view(request):
    print("Views User")
    my_projects = Project.objects.filter(assign = request.user.id).order_by("id")
    my_tasks = Task.objects.filter(assign = request.user.id).order_by("id")

    context = {
        'projects' : my_projects,
        'tasks' : my_tasks,
    }
    return render(request, "views/user-view.html", context)