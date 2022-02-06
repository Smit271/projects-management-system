from email.policy import default
from django.db import models
from django.contrib.auth.models import User

employment_type = (
    ('1', 'Employee'),
    ('2', 'Intern'),
)

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=8, choices=employment_type, default = 1)
    img    = models.ImageField(upload_to='core/staic/core/avatar', blank=True, default='core/avatar/blank_profile.png')

    def __str__(self):
        return str(self.user.email)