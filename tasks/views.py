from rest_framework import generics, permissions, filters
from smart_work_api.permissions import IsOwnerOrReadOnlyTask
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Need to add permissions where a user can only create a task
# if they are a member of the corresponding project
class TaskList(generics.ListCreateAPIView):
    """
    List tasks or create a task if logged in.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'assigned_to',
        'assigned_to__project',
        'assigned_to__profile',
    ]


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a task, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnlyTask]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
