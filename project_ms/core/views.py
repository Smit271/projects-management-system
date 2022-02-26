from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project, Task
from user.models import User, UserProfile

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def dashboard(request):
    res = {}
    projects = Project.objects.all().count()
    task = Task.objects.all().count()
    active_proeject = Project.objects.filter(status__in = ["2", "3"]).count()
    res["project"] = projects
    res["task"] = task
    res["active_proeject"] = active_proeject
    # print(active_proeject)
    # print(res)
    return render(request, "core/dashboard.html", context=res)

def context(request): # send context to base.html
    # if not request.session.session_key:
    #     request.session.create()
    users = User.objects.all()
    users_prof = UserProfile.objects.all()
    if request.user.is_authenticated:
        try:
            users_prof = UserProfile.objects.exclude(
                id=request.user.userprofile_set.values_list()[0][0])  # exclude himself from invite list
            user_id = request.user.userprofile_set.values_list()[0][0]
            logged_user = UserProfile.objects.get(id=user_id)
            context = {
                'users': users,
                'users_prof': users_prof,
                'logged_user': logged_user,
            }
            return context
        except:
            users_prof = UserProfile.objects.all()
            context = {
                'users':users,
                'users_prof':users_prof,
            }
            return context
    else:
        context = {
            'users': users,
            'users_prof': users_prof,
        }
        return context
    