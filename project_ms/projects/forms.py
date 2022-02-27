from tkinter import Widget
from django import forms
from django.utils.text import slugify
from .models import Task, Project
from django.contrib.auth.models import User

status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)


class TaskRegistrationForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name = forms.CharField(max_length=80)
    status = forms.ChoiceField(choices=status)
    due = forms.ChoiceField(choices=due)
    description = forms.CharField(widget=forms.Textarea)
    deadline = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = '__all__'


    def save(self, commit=True):
        task = super(TaskRegistrationForm, self).save(commit=False)
        task.project = self.cleaned_data['project']
        task.task_name = self.cleaned_data['task_name']
        task.status = self.cleaned_data['status']
        task.due = self.cleaned_data['due']
        task.deadline = self.cleaned_data['deadline']
        task.description = self.cleaned_data['description']
        task.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            task.assign.add((assign))

        if commit:
            task.save()

        return task


    def __init__(self, *args, **kwargs):
        super(TaskRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Project Name'
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'Task'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['due'].widget.attrs['class'] = 'form-control'
        self.fields['due'].widget.attrs['placeholder'] = 'Due type'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Assign'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['placeholder'] = 'Deadline'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe in detail'


class ProjectRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    project_lead = forms.ModelChoiceField(queryset=User.objects.all())
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    # efforts = forms.DurationField()
    status = forms.ChoiceField(choices=status)
    complete_per = forms.FloatField(min_value=0, max_value=100)
    description = forms.CharField(widget=forms.Textarea)
    deadline = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Project
        fields = '__all__'


    def save(self, commit=True):
        Project = super(ProjectRegistrationForm, self).save(commit=False)
        Project.name = self.cleaned_data['name']
        Project.project_lead = self.cleaned_data['project_lead']
        # Project.efforts = self.cleaned_data['efforts']
        Project.status = self.cleaned_data['status']
        Project.deadline = self.cleaned_data['deadline']
        Project.complete_per = self.cleaned_data['complete_per']
        Project.description = self.cleaned_data['description']
        # Project.slug = slugify(str(self.cleaned_data['name']))
        Project.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            Project.assign.add((assign))

        if commit:
            Project.save()

        return Project


    def __init__(self, *args, **kwargs):
        super(ProjectRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Project Name'
        self.fields['project_lead'].widget.attrs['class'] = 'form-control'
        self.fields['project_lead'].widget.attrs['placeholder'] = 'Lead'
        # self.fields['efforts'].widget.attrs['class'] = 'form-control'
        # self.fields['efforts'].widget.attrs['placeholder'] = 'Efforts'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['placeholder'] = 'Dead-Line'
        # self.fields['company'].widget.attrs['class'] = 'form-control'
        # self.fields['company'].widget.attrs['placeholder'] = 'Company'
        self.fields['complete_per'].widget.attrs['class'] = 'form-control'
        self.fields['complete_per'].widget.attrs['placeholder'] = 'Complete %'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'
        self.fields['assign'].widget.attrs['class'] = 'form-control'

class ProjectUpdateForm(forms.ModelForm):

    name = forms.CharField(max_length=80)
    project_lead = forms.ModelChoiceField(queryset=User.objects.all())
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    # efforts = forms.DurationField()
    status = forms.ChoiceField(choices=status)
    complete_per = forms.FloatField(min_value=0, max_value=100)
    description = forms.CharField(widget=forms.Textarea)
    deadline = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProjectUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Project Name'
        self.fields['project_lead'].widget.attrs['class'] = 'form-control'
        self.fields['project_lead'].widget.attrs['placeholder'] = 'Lead'
        # self.fields['efforts'].widget.attrs['class'] = 'form-control'
        # self.fields['efforts'].widget.attrs['placeholder'] = 'Efforts'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['placeholder'] = 'Dead-Line'
        # self.fields['company'].widget.attrs['class'] = 'form-control'
        # self.fields['company'].widget.attrs['placeholder'] = 'Company'
        self.fields['complete_per'].widget.attrs['class'] = 'form-control'
        self.fields['complete_per'].widget.attrs['placeholder'] = 'Complete %'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Type here the project description...'
        self.fields['assign'].widget.attrs['class'] = 'form-control'


class TaskUpdateForm(forms.ModelForm):

    project = forms.ModelChoiceField(queryset=Project.objects.all())
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name = forms.CharField(max_length=80)
    status = forms.ChoiceField(choices=status)
    due = forms.ChoiceField(choices=due)
    description = forms.CharField(widget=forms.Textarea)
    deadline = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskUpdateForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Project Name'
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'Task'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Status'
        self.fields['due'].widget.attrs['class'] = 'form-control'
        self.fields['due'].widget.attrs['placeholder'] = 'Due type'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Assign'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['placeholder'] = 'Deadline'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe in detail'