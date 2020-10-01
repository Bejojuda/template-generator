from django.urls import path
from .views import AccountView, AccountDetailsView


urlpatterns = [
    path('', AccountView.as_view()),
    path('<uuid:uuid>/', AccountDetailsView.as_view())
]