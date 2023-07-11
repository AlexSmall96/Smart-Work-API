from django.db import models
from django.contrib.auth.models import User
from .models import Profile

class Member(models.Model):
    """

    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
