from rest_framework import serializers

from variable.serializers import VariableViewSerializer
from .models import Template


class TemplateSerializer(serializers.ModelSerializer):
    variables = VariableViewSerializer(many=True, read_only=True)

    class Meta:
        model = Template
        fields = '__all__'


class TemplateDetailsSerializer(serializers.ModelSerializer):

    document = serializers.FileField(read_only=True)

    class Meta:
        model = Template
        fields = '__all__'
