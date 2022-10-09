from django import forms
from django.contrib.auth.models import User


class MensajeForm(forms.Form):
    contenido = forms.CharField(max_length=1000, widget=forms.Textarea)
    receptor = forms.ModelChoiceField(queryset=User.objects.all())


class ResponderForm(forms.Form):
    contenido = forms.CharField(max_length=1000, widget=forms.Textarea)