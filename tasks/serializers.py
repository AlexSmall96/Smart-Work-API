from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'project', 'start_date', 'due_date', 'description',
            'status'
        ]

class TaskDetailSerializer(TaskSerializer):
    """
    Serializer for the Task model used in Detail view
    Project is a read only field so that we dont have to set it on each update
    """
    project = serializers.ReadOnlyField(source='project.id')