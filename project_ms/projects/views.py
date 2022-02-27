from django.shortcuts import redirect, render
from projects.models import Project, Task
from django.db.models import Avg
from projects.forms import ProjectRegistrationForm, TaskRegistrationForm, ProjectUpdateForm, TaskUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

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
    # print(id)
    project = Project.objects.filter(id = id).first()
    # my_projects = Project.objects.filter(assign = request.user.id)
    # my_tasks = Task.objects.filter(assign = request.user.id)
    # avg_projects = Project.objects.filter(assign = request.user.id).aggregate(Avg('complete_per'))['complete_per__avg']
    # overdue_tasks = my_tasks.filter(due='2')
    a = list(User.objects.filter(project_assign = id).values_list("first_name", flat = True))
    task = Task.objects.filter(project_id = id).all()
    task_details = []
    # print(task)
    overdue_count = 0
    for i in task:
        if i.due == '2':
            overdue_count = overdue_count + 1
        # print(f"id : {i.id}, status {i.status}")
        b= list(User.objects.filter(task_assign = i.id).values_list("first_name", flat= True))
        # b = list(User.objects.filter(task__task_assign = i.id).values_list("username", flat = True))
        task_detail = {}
        task_detail['name'] = i.task_name
        task_detail['status'] = i.status
        task_detail['desc'] = i.description
        task_detail['assigned'] = b
        task_detail['deadline'] = i.deadline
        task_details.append(task_detail)
        # print(task_detail)
        
    context = {
        'id' : id,
        'name' : project.name,
        'description' : project.description,
        'status' : project.status,
        'team' : a,
        'lead' : project.project_lead.first_name + " " + project.project_lead.last_name,
        'deadline' : project.deadline,
        'complete_per' : project.complete_per,
        'task_overdue_count' : overdue_count,
        'task' : task_details
    }
    return render(request, 'projects/projects-detail.html', context)

@login_required
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
        
@login_required
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

@login_required
def UpdateProject(request, id):
    if request.method == 'POST':
        obj = Project.objects.get(pk = id)
        u_form = ProjectUpdateForm(request.POST, instance=obj)
        context = {'form': u_form}
        if u_form.is_valid():
            u_form.save()
            messages.success(request, ('Project details updated Successfully'))
            return redirect(reverse('views:users-view'))
        else:
            return render(request, 'projects/update-project.html', context)
    else:
        obj = Project.objects.get(pk = id)
        u_form = ProjectUpdateForm(instance=obj)
        context = {
            'form': u_form,
        }
        return render(request,'projects/update-project.html', context)

@login_required
def UpdateTask(request, id):
    if request.method == 'POST':
        obj = Task.objects.get(pk = id)
        u_form = TaskUpdateForm(request.POST, instance=obj)
        context = {'form': u_form}
        if u_form.is_valid():
            u_form.save()
            messages.success(request, ("Task's details updated Successfully"))
            return redirect(reverse('views:users-view'))
        else:
            return render(request, 'projects/update-task.html', context)
    else:
        obj = Task.objects.get(pk = id)
        u_form = TaskUpdateForm(instance=obj)
        context = {
            'form': u_form,
        }
        return render(request,'projects/update-task.html', context)