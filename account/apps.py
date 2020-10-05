from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    import account.services
