from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model
    Adds three extra fields when returning a list of Task instances
    """
    project_title = serializers.ReadOnlyField(
        source='assigned_to.project.title')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    assigned_to_username = serializers.ReadOnlyField(
        source='assigned_to.profile.owner.username')
    assigned_to_profile_id = serializers.ReadOnlyField(
        source='assigned_to.profile.id')
    assigned_to_image = serializers.ImageField(
        source='assigned_to.profile.image',
        read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
