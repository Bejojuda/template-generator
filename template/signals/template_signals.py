from django.db.models.signals import post_save
from django.dispatch import receiver
from template.models import Template


@receiver(post_save, sender=Template)
def get_variables(sender, **kwargs):
    print('hOLA')
    if kwargs.get('created', False):
        print(kwargs['instance'])