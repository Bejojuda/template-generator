from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .settings import SIMPLE_JWT


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)

        data.update({'user': self.user.username})
        data.update({'uuid': self.user.account.uuid})
        token_time = SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds /60

        data['token_life_time'] = str(token_time) + ' minutes'

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
