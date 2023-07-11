from rest_framework import generics, permissions
from smart_work_api.permissions import IsOwnerOrReadOnly
from .models import Project
from .serializers import ProjectSerializer


class ProjectList(generics.ListCreateAPIView):
    """
    List projects or create a project if logged in
    The perform_create method associates the project with the logged in user.
    """
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a project and edit or delete it if you own it.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Project.objects.all()