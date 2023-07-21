from django.db import IntegrityError
from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    """
    Serializer for the Member model
    Create method handles the unique constraint on 'owner' and 'followed'
    """
    owner = serializers.ReadOnlyField(source='profile.owner.username')
    member_name = serializers.ReadOnlyField(source='profile.name')
    project_title = serializers.ReadOnlyField(source='project.title')
   
    class Meta:
        model = Member
        fields = '__all__'

    def create(self, validated_data):
        return Member.objects.create(**validated_data)