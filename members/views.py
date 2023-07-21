from rest_framework import generics, permissions
from smart_work_api.permissions import IsOwnerOrReadOnly
from .models import Member
from projects.models import Project
from .serializers import MemberSerializer


class MemberList(generics.ListCreateAPIView):
    """
    List all Members, i.e. all instances of a user
    assigned to a project.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

