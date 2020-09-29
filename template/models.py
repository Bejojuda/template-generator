import uuid
from django.db import models


class Template(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    document = models.FileField()
