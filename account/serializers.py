from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=10)
    firstname = serializers.CharField(max_length=25, source='account.firstname')
    lastname = serializers.CharField(max_length=25, source='account.lastname')
    position = serializers.CharField(max_length=40, source='account.position')
    uuid = serializers.UUIDField(source='account.uuid', read_only=True)

    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'}
                                     )

    class Meta:
        model = User
        fields = ['uuid', 'username', 'password', 'firstname', 'lastname', 'position']

    def create(self, validated_data):
        account = validated_data.pop('account')

        validated_data['password'] = make_password(validated_data['password'])

        user = User.objects.create(**validated_data)
        Account.objects.create(**account, user=user)

        return user


class AccountDetailsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=10)
    firstname = serializers.CharField(max_length=25, source='account.firstname')
    lastname = serializers.CharField(max_length=25, source='account.lastname')
    position = serializers.CharField(max_length=40, source='account.position')
    uuid = serializers.UUIDField(source='account.uuid', read_only=True)

    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'},
                                     required=False
                                     )

    class Meta:
        model = User
        fields = ['uuid', 'username', 'password', 'firstname', 'lastname', 'position']

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
            instance.password = validated_data.get('password', instance.password)

        if 'username' in validated_data:
            instance.username = validated_data.get('username', instance.username)

        instance.save()
        return instance
