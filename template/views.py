import re
from io import BytesIO
from wsgiref.util import FileWrapper

from django.http import HttpResponse
from docx import Document
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import Template
from .serializers import TemplateSerializer, TemplateDetailsSerializer, TemplateFillOutSerializer
from general.pagination import LargeResultsSetPagination
from .services import replace_variables


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


class TemplateFillOutView(generics.UpdateAPIView, generics.RetrieveAPIView):
    """
    View to fill out a template
    """
    serializer_class = TemplateFillOutSerializer
    queryset = Template.objects.all()

    lookup_field = 'uuid'

    def put(self, request, *args, **kwargs):
        template = Template.objects.get(uuid__exact=self.kwargs['uuid'])
        print(request.data)
        doc = Document(template.document)
        document = replace_variables(doc, request.data['sent_variables'])
        print(request.data)
        f = BytesIO()
        document.save(f)
        file_handle = template.document.open()

        # send file
        # response = FileResponse(file_handle, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        f.seek(0)
        response = HttpResponse(f.getvalue(),
                                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="%s"' % template.name

        return response


