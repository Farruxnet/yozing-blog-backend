from rest_framework import serializers

from yozing.models import Yozing


class YozingGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yozing
        fields = '__all__'


class YozingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yozing
        fields = []

    def create(self, validated_data):
        data = super().create(validated_data=validated_data)
        return data


class YozingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yozing
        fields = []

    def update(self, instance, validated_data):
        data = super().update(instance, validated_data)
        return data
