from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from projects.models import Project

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
    return render(request, "views/index.html")