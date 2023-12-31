from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
from profiles.models import Profile


class Member(models.Model):
    """
    Creates an instance of a user assigned to a project
    uses profile and project data.
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile.name} {self.project}'

    class Meta:
        ordering = ['-created_at']
        unique_together = ['profile', 'project']

