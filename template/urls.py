from django.urls import path
from .views import TemplateView, TemplateDetailsView, TemplateFillOutView, TemplateRenameFileView


urlpatterns = [
    path('', TemplateView.as_view()),
    path('<uuid:uuid>', TemplateDetailsView.as_view()),
    path('fillout/<uuid:uuid>', TemplateFillOutView.as_view()),
    path('rename_file/<uuid:uuid>', TemplateRenameFileView.as_view()),
]