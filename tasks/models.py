from django.db import models
from django.contrib.auth.models import User
from members.models import Member


class Task(models.Model):
    """
    Task model, related to member (assigned_to)
    """
    assigned_to = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    description = models.TextField(null=False, blank=False)
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
