from rest_framework import generics, permissions, filters
from smart_work_api.permissions import IsOwnerOrReadOnly
from .models import Member
from projects.models import Project
from .serializers import MemberSerializer
from django_filters.rest_framework import DjangoFilterBackend

class MemberList(generics.ListCreateAPIView):
    """
    List all Members, i.e. all instances of a user
    assigned to a project.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'profile'
    ]

