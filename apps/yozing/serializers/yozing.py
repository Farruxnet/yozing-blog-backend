from rest_framework import serializers

from helpers.serializers.categories import CategorySerializer
from helpers.serializers.tags import TagSerializer
from yozing.models import Yozing


class YozingListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    text = serializers.SerializerMethodField()

    class Meta:
        model = Yozing
        fields = ['id', 'name', 'text', 'categories', 'image', 'created_at', 'created_by']

    def get_text(self, obj):
        return ' '.join(obj.text.split()[:25])


class YozingDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Yozing
        fields = ['id', 'name', 'text', 'categories', 'tags', 'image', 'created_by', 'created_at']


class YozingMyPostDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Yozing
        fields = ['id', 'name', 'text', 'categories', 'tags', 'image', 'created_by', 'created_at']


class YozingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yozing
        fields = ['name', 'text', 'categories', 'tags', 'image', ]

    def create(self, validated_data):
        data = super().create(validated_data=validated_data)
        return data


class YozingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yozing
        fields = ['id', 'name', 'text', 'tags', 'categories', 'image']

    def update(self, instance, validated_data):
        data = super().update(instance, validated_data)
        return data
