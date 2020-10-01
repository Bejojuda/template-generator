from django.urls import path
from .views import TemplateView, TemplateDetailsView, TemplateFillOutView


urlpatterns = [
    path('', TemplateView.as_view()),
    path('<uuid:uuid>', TemplateDetailsView.as_view()),
    path('fillout/<uuid:uuid>', TemplateFillOutView.as_view()),
]