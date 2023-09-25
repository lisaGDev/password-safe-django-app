from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Password(models.Model):
    data_created = models.DateField(null=True)
    time = models.TimeField(null=True)
    app_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

def __str__(self):
    return f"{self.id} {self.data_created} {self.time} {self.app_name} {self.username} {self.password} {self.type}"
