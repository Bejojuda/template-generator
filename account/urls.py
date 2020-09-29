from django.urls import path
from .views import AccountView, AccountDetailsView


urlpatterns = [
    path('', AccountView.as_view()),
    path('<uuid:account__uuid>/', AccountDetailsView.as_view())
]