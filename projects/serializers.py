from rest_framework import serializers
from projects.models import Project
from members.models import Member


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model
    Adds several read only fields from profile data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Project
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'start_date', 'due_date',
            'title', 'description', 'complexity'
        ]
