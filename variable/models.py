import uuid as uuid
from django.db import models


class Variable(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=50, null=True)
    template = models.ForeignKey(to='template.Template', on_delete=models.CASCADE, related_name='variables')
    optional = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name) + '('+str(self.template)+')'
