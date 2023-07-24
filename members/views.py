from rest_framework import generics, permissions, filters
from smart_work_api.permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyMember
from .models import Member
from projects.models import Project
from profiles.models import Profile
from .serializers import MemberSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404

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
        'profile',
        'project'
    ]

    def create_member(sender, instance, created, **kwargs):
        project = get_object_or_404(Project, pk=instance.id)
        profile = get_object_or_404(Profile, pk=instance.owner.id)
        member = Member.objects.create(project=project, profile=profile)
        member.save()
        
    post_save.connect(receiver=create_member, sender=Project)


class MemberDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a Member
    Destroy a member, i.e. remove user from project
    """
    permission_classes = [IsOwnerOrReadOnlyMember]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
