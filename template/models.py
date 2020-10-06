import os
import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from docx import Document

from account.models import Account
from .services import search_variables, create_variables, search_optional_variables, get_upload_path
from .validators import validate_file_extension


class Template(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=30)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(null=True, blank=True)
    document = models.FileField(validators=[validate_file_extension], upload_to=get_upload_path)
    status = models.CharField(max_length=10, choices=(
        ('INA', 'Inactive'),
        ('ACT', 'Active')
    ), default='INA')
    creator = models.ForeignKey(Account, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Template)
def get_variables(sender, **kwargs):
    """
    Signal that calls search_variables and create_variables everytime a template is created
    """
    if kwargs.get('created', False):
        template = kwargs['instance']
        document = Document(template.document)
        variables = search_variables(document)
        optional_variables = search_optional_variables(document)
        create_variables(template, variables, optional_variables)





