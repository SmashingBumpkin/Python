from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
