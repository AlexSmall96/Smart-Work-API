from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """
    Project model, related to 'owner', i.e. a User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    complexity = models.CharField(
        max_length=7, 
        choices=(
            ('Low', 'LOW'),
            ('Medium', 'MEDIUM'),
            ('High', 'HIGH'),
        ),
        default='Low'
    )


    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f'{self.id} {self.title}'