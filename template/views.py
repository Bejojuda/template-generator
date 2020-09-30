import re

from docx import Document
from rest_framework import generics
from .models import Template
from .serializers import TemplateSerializer, TemplateDetailsSerializer
from general.pagination import LargeResultsSetPagination


class TemplateView(generics.ListCreateAPIView):
    """
    List all the Templates
    """
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()
    pagination_class = LargeResultsSetPagination


class TemplateDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    View details of specific template
    """
    serializer_class = TemplateDetailsSerializer
    queryset = Template.objects.all()

    lookup_field = 'uuid'


