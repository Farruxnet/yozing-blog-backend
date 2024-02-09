from rest_framework import serializers

from users.models import User, Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'phone_number']


class LoginSerializer(serializers.Serializer):
    otp_code = serializers.IntegerField(required=True, max_value=999999, min_value=100000)

    class Meta:
        model = User
        fields = ('otp_code',)


class JwtSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def to_representation(self, instance):
        instance = super().to_representation(instance)
        return instance

    class Meta:
        model = Token
        fields = ('jwt', 'user')
        read_only_fields = ['jwt', 'user']
