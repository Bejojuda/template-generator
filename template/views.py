import os

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from .models import Template
from .serializers import TemplateSerializer, TemplateDetailsSerializer, TemplateFillOutSerializer, TemplateRenameFileSerializer
from general.pagination import LargeResultsSetPagination
from .services import generate_document, rename_file


class TemplateView(generics.ListCreateAPIView):
    """
    List all the Templates
    """
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()
    pagination_class = LargeResultsSetPagination
    """
    def get_queryset(self):
        queryset = Template.objects.all()
        template = queryset.first()

        rename_file("Le new Docú.docx", template)

        # os.rename(template.document.path, "Nuevo.docx")
        print(os.path.basename(template.document.name))
     """
    """
    def get_queryset(self):
        pythoncom.CoInitialize()

        queryset = Template.objects.all()
        template = queryset.first()

        w = wc.Dispatch('Word.Application')
        path = os.path.join('media', template.document.path)
        print(path)
        doc = w.Documents.Open(path)
        print(doc.__dict__)
        path = os.path.join(path, 'Nuevo DOC.doc')
        doc.SaveAs('Formato.doc', 16)
        print(template.document.name)
        return queryset
    """


class TemplateDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    View details of specific template
    """
    serializer_class = TemplateDetailsSerializer
    queryset = Template.objects.all()

    lookup_field = 'uuid'

    def put(self, request, *args, **kwargs):
        template = Template.objects.get(uuid__exact=self.kwargs['uuid'])
        rename_file("hh", template)


class TemplateFillOutView(generics.UpdateAPIView, generics.RetrieveAPIView):
    """
    View to fill out a template
    """
    serializer_class = TemplateFillOutSerializer
    queryset = Template.objects.all()

    lookup_field = 'uuid'

    def put(self, request, *args, **kwargs):
        template = Template.objects.get(uuid__exact=self.kwargs['uuid'])
        response = generate_document(request.data, template)

        return response


class TemplateRenameFileView(generics.UpdateAPIView, generics.RetrieveAPIView):
    serializer_class = TemplateRenameFileSerializer
    queryset = Template.objects.all()

    lookup_field = 'uuid'

    def put(self, request, *args, **kwargs):
        template = Template.objects.get(uuid__exact=self.kwargs['uuid'])
        templates = Template.objects.all()
        res = rename_file(request.data['filename'], template, templates)

        response = Response({
            "filename": res
        })

        return response


