from django.urls import path
from .views import TemplateView, TemplateDetailsView


urlpatterns = [
    path('', TemplateView.as_view()),
    path('<uuid:uuid>', TemplateDetailsView.as_view())
]