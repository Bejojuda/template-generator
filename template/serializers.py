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
    creator = serializers.CharField(source='creator.user.username', read_only=True)

    class Meta:
        model = Template
        fields = '__all__'


class TemplateFillOutSerializer(serializers.ModelSerializer):
    document = serializers.FileField(read_only=True)
    creator = serializers.CharField(source='creator.user.username', read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    update_date = serializers.DateField(read_only=True)
    status = serializers.CharField(read_only=True)
    sent_variables = serializers.JSONField(write_only=True)
    variables = VariableViewSerializer(many=True, read_only=True)

    class Meta:
        model = Template
        fields = '__all__'


class TemplateRenameFileSerializer(serializers.ModelSerializer):
    file = serializers.CharField(source='filename', max_length=20, read_only=True)
    filename = serializers.CharField(source='document.name', max_length=20, write_only=True)

    class Meta:
        model = Template
        fields = ['filename', 'file']
