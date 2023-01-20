from .models import Pessoa
from django import forms



class PersonData(forms.Form):
    class meta:
        model = Pessoa
        fields = '__all__'
