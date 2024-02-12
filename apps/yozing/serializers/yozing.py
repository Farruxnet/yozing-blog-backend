from rest_framework import serializers

from yozing.models import Yozing


class YozingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yozing
        fields = ['name', 'text', 'categories', 'created_at', 'created_by']


class YozingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yozing
        fields = ['name', 'text', 'categories', 'tags', 'created_by', 'created_at']


class YozingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yozing
        fields = ['name', 'text', 'categories', 'tags']

    def create(self, validated_data):
        data = super().create(validated_data=validated_data)
        return data


class YozingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yozing
        fields = ['id', 'name', 'text', 'tags', 'categories']

    def update(self, instance, validated_data):
        data = super().update(instance, validated_data)
        return data
