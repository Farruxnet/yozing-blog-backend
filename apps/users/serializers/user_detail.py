from rest_framework import serializers

from users.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name',
            'phone_number',
            'email',
            'telegram_id',
            'image',
            'linkedin_url',
            'github_url',
            'instagram_url',
            'facebook_url',
            'date_joined'
        ]
        