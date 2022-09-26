from django import forms



class MensajeForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()
    nacimiento = forms.DateField()
    documento = forms.IntegerField()