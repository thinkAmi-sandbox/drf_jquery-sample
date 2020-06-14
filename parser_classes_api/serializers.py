from rest_framework import serializers

from parser_classes_api.models import Apple, AppleJsonOnly


class AppleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apple
        fields = '__all__'


class AppleJsonOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppleJsonOnly
        fields = '__all__'
