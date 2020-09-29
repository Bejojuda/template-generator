import uuid

from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')

    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    position = models.CharField(max_length=45)

    def __str__(self):
        return self.user.username

