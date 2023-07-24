from rest_framework import generics, permissions
from smart_work_api.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer


# Need to add permissions where a user can only create a task
# if they are a member of the corresponding project
class TaskList(generics.ListCreateAPIView):
    """
    List tasks or create a task if logged in.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a task, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
