from django import forms

from coursesapp import models as coursesapp_models


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=coursesapp_models.Course.objects.all(), widget=forms.HiddenInput)
