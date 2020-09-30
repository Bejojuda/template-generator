import re

from variable.models import Variable


def search_variables(document):
    """
    Search and return all of the variables in the document.
    A variable has this format: {{variable_name}}
    """
    variables = []
    for p in document.paragraphs:
        variables += re.findall(r"\{\{(.[^{}]*?)\}\}", p.text)
    return variables


def create_variables(template, variables_str=[]):
    """
    Receives a list of variables and a template, and then creates the variable objects and the relationship
    with the template object
    """
    for v in variables_str:
        variable = Variable.objects.create(name=v, template=template)
        template.variables.add(variable)