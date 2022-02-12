from django.shortcuts import render
from projects.models import Project, Task
from django.db.models import Avg
from projects.forms import ProjectRegistrationForm, TaskRegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(due='2')
    # full = []
    # project_dict = {}
    # for i in projects:
    #     a = list(User.objects.filter(project__assign = i.id).values_list("username", flat = True))
    #     project_dict['name'] = i.name
    #     project_dict['lead'] = i.project_lead.first_name + " " + i.project_lead.last_name
    #     project_dict['team'] = a
    #     project_dict['progress'] = i.complete_per
    #     project_dict['desc'] = i.description
    #     print(project_dict)
    #     full.append(project_dict)
        # print(a)
    # temp = Project.objects.all().values_list("assign")
    # temp = Task.objects.filter(assign = request.user.id)
    # print(temp)
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
    }
    return render(request, 'projects/projects.html', context)

def ProjectDetail(request, id):
    print(id)
    project = Project.objects.filter(id = id).first()
    # my_projects = Project.objects.filter(assign = request.user.id)
    # my_tasks = Task.objects.filter(assign = request.user.id)
    # avg_projects = Project.objects.filter(assign = request.user.id).aggregate(Avg('complete_per'))['complete_per__avg']
    # overdue_tasks = my_tasks.filter(due='2')
    a = list(User.objects.filter(project__assign = id).values_list("first_name", flat = True))
    task = Task.objects.filter(project_id = id).all()
    print(task)
    for i in task:
        print(f"id : {i.id}, status {i.status}")
        b= list(User.objects.filter(task_assign = i.id).values_list("first_name", flat= True))
        # b = list(User.objects.filter(task__task_assign = i.id).values_list("username", flat = True))
        task_detail = {}
        task_detail['desc'] = i.description
        task_detail['assigned'] = b
        print(task_detail)
        
    context = {
        'id' : id,
        'name' : project.name,
        'description' : project.description,
        'status' : project.status,
        'team' : a,
        'lead' : project.project_lead.first_name + " " + project.project_lead.last_name,
        'deadline' : project.deadline,
        'complete_per' : project.complete_per,
        'task' : task
    }
    return render(request, 'projects/projects-detail.html', context)


def CreateProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/create-project.html', context)
        else:
            return render(request, 'projects/create-project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/create-project.html', context)

def CreateTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/create-task.html', context)
        else:
            return render(request, 'projects/create-task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/create-task.html', context)
