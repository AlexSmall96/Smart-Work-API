from django.db import models
from django.contrib.auth.models import User
from members.models import Member


class Task(models.Model):
    """
    Task model, related to User and Project
    """
    # owner foreign key could be changed to member of project
    # owner is who creates the task
    assigned_to = models.ForeignKey(Member, on_delete=models.CASCADE)
    # Add validation for start_date and due_date
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=11,
        choices=(
            ('Not Started', 'NOT STARTED'),
            ('In Progress', 'IN PROGRESS'),
            ('Complete', 'COMPLETE'),
        ),
        default='Not Started'
    )
   
    class Meta:
        ordering = ['due_date']


    def __str__(self):
        return self.content