from django.urls import path
from .views import AccountView, AccountDetailsView, AccountCreateView


urlpatterns = [
    path('', AccountView.as_view()),
    path('register/', AccountCreateView.as_view()),
    path('<uuid:uuid>/', AccountDetailsView.as_view())
]