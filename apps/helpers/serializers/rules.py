from rest_framework import serializers

from helpers.models import Rules


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = ['terms_of_use', 'privacy_policy', 'cookie_policy']
        read_only_fields = fields
