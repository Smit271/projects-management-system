from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=48, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    confirm_pass = models.CharField(max_length=20)

    def __str__(self):
        return self.email_id