from django.db import models
from remedios.models import Remedio
from django import forms


class FormRemedio(forms.ModelForm):
    class Meta:
        model = Remedio
        exclude = ()


