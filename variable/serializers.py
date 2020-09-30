from rest_framework import serializers

from variable.models import Variable


class VariableViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variable
        fields = ['uuid', 'name']
