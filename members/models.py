from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
from profiles.models import Profile


class Member(models.Model):
    """
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.profile.name} {self.project}'