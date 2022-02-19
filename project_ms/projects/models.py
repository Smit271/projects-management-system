from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

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


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=80)
    project_lead = models.ForeignKey(User, on_delete=models.CASCADE)
    assign = models.ManyToManyField(User, related_name="project_assign")
    # efforts = models.DurationField()
    status = models.CharField(max_length=7, choices=status, default=1)
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(blank=True)
    deadline = models.DateField()

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="task_project_assign")
    assign = models.ManyToManyField(User, related_name="task_assign")
    task_name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=1)
    due = models.CharField(max_length=7, choices=due, default=1)
    description = models.TextField(blank=True)
    deadline = models.DateField()

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)

# class ProjectAssign(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'project_assign_user'

#     def __str__(self) -> str:
#         return f"{self.user_id} with project {self.project_id}"