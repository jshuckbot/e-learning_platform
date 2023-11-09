from django import forms
from django.forms.models import inlineformset_factory

from coursesapp import models as coursesapp_models

ModuleFormSet = inlineformset_factory(
    coursesapp_models.Course, coursesapp_models.Module, fields=("title", "description"), extra=2, can_delete=True
)
