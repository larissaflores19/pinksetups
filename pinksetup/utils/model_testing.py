"""
Returns a dict with a model fields
"""
from django.contrib.auth.models import User

from pinksetup.models import Post


def get_model_fields(model, instance):
    field_names = [f.name for f in model._meta.fields]
    property_names = [name for name in dir(model) if isinstance(getattr(model, name), property)]
    return dict((name, getattr(instance, name)) for name in field_names + property_names)
