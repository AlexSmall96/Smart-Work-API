from django.db import IntegrityError
from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    """
    Serializer for the Member model
    Adds several read only fields from projects and profiles
    """
    member_name = serializers.ReadOnlyField(source='profile.name')
    member_username = serializers.ReadOnlyField(
        source='profile.owner.username')
    member_image = serializers.ImageField(
        source='profile.image',
        read_only=True)
    title = serializers.ReadOnlyField(source='project.title')
    description = serializers.ReadOnlyField(source='project.description')
    start_date = serializers.ReadOnlyField(source='project.start_date')
    due_date = serializers.ReadOnlyField(source='project.due_date')
    project_owner_image = serializers.ImageField(
        source='project.owner.profile.image',
        read_only=True)
    project_owner_profile_id = serializers.ReadOnlyField(
        source='project.owner.profile.id')
    project_owner_name = serializers.ReadOnlyField(
        source='project.owner.profile.name')
    project_owner_username = serializers.ReadOnlyField(
        source='project.owner.username')
    complexity = serializers.ReadOnlyField(source='project.complexity')

    class Meta:
        model = Member
        fields = '__all__'

    def create(self, validated_data):
        return Member.objects.create(**validated_data)
