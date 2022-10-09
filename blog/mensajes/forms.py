from django import forms
from django.contrib.auth.models import User


class MensajeForm(forms.Form):
    receptor = forms.ModelChoiceField(queryset=User.objects.all().exclude(username="admin"))
    contenido = forms.CharField(max_length=1000, widget=forms.Textarea)