from dal import autocomplete

from django import forms

from .models import Country
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('__all__')
        widgets = {
            'birth_country': autocomplete.ModelSelect2(url='country-autocomplete')
        }
