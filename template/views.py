from io import BytesIO

from django.http import HttpResponse
from docx import Document
from rest_framework import generics

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
        """
        When a PUT is made with 'sent_variables', a new .docx is generated with said variables added to the document.
        The document is returned to be downloaded by the user.
        """
        template = Template.objects.get(uuid__exact=self.kwargs['uuid'])
        doc = Document(template.document)

        sent_variables = request.data['sent_variables']
        optional_variables = {}

        if 'optional_variables' in request.data:
            optional_variables = request.data['optional_variables']

        document = replace_variables(doc, sent_variables, optional_variables)

        f = BytesIO()
        document.save(f)
        response = HttpResponse(f.getvalue(),
                                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="%s"' % template.name

        return response


