from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .services.account_services import check_emails
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=10, source='user.username')

    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'},
                                     source='user.password'
                                     )

    class Meta:
        model = Account
        fields = ['uuid', 'username', 'email', 'password', 'firstname', 'lastname', 'position']

    def create(self, validated_data):
        """
        Checks if the provided E-mail is among the company's employees list, if authorized,
        a hashed password is generated and saved to the database
        """
        email = validated_data['email']
        if not check_emails(email):
            raise ValidationError({"error": "E-mail does not belong to company employee"})
        elif Account.objects.filter(email=email).exists():
            raise ValidationError({"error": "A user with this E-mail already exists"})

        user = validated_data.pop('user')

        user['password'] = make_password(user['password'])

        user = User.objects.create(**user)
        account = Account.objects.create(**validated_data, user=user)

        return account


class AccountDetailsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=10, source='user.username')

    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'},
                                     required=False,
                                     source='user.password'
                                     )

    class Meta:
        model = Account
        fields = ['uuid', 'username', 'password', 'firstname', 'lastname', 'position', 'creator']

    def update(self, instance, validated_data):
        """
        Updates user information
        """
        user_data = validated_data.pop('user')
        user = User.objects.get(username=instance.user.username)

        if 'password' in user_data:
            user_data['password'] = make_password(user_data['password'])
            user.password = user_data.get('password', user.password)
            instance.user.password = user_data.get('password', user.password)
            print(instance.user.password)

        if 'username' in user_data:
            if not User.objects.filter(username=user_data['username']):
                user.username = user_data.get('username', user.username)
                instance.user.username = user_data.get('username', user.username)
            elif user_data['username'] == instance.user.username:
                pass
            else:
                raise ValidationError({
                    'message': 'This username already exists'
                })
        user.save()

        if 'firstname' in validated_data:
            instance.firstname = validated_data['firstname']
        if 'lastname' in validated_data:
            instance.lastname = validated_data['lastname']
        if 'position' in validated_data:
            instance.position = validated_data['position']

        instance.save()
        return instance
