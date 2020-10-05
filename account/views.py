from rest_framework import generics

from .models import Account
from .serializers import AccountSerializer, AccountDetailsSerializer
from general.pagination import StandardResultsSetPagination


class AccountView(generics.ListAPIView):
    """
    List all of the registered Accounts
    """
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    pagination_class = StandardResultsSetPagination


class AccountCreateView(generics.CreateAPIView):
    """
    Create a new Account
    """
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get specific Account by uuid
    """
    serializer_class = AccountDetailsSerializer
    lookup_field = 'uuid'
    queryset = Account.objects.all()

