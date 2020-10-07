import os

from django.core.exceptions import ValidationError


def validate_file_extension(value):
    from template.models import Template
    templates = Template.objects.all()

    for t in templates:
        if t.filename() == value.name:
            raise ValidationError("Un documento con este nombre ya existe")

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError("Tipo de archivo no permitido")
