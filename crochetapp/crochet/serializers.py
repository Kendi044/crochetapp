from rest_framework import serializers
from .models import Pattern
from django.contrib.auth import get_user_model

User = get_user_model()


class PatternSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Pattern
        fields = [
            'id',
            'title',
            'description',
            'instructions',
            'difficulty_level',
            'is_public',
            'user',
            'user_name',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['user']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value
