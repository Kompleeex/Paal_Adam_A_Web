import django_filters as filter
from django import forms
from .models import *

class tesztFilter(filter.FilterSet):
    kategoriaID = filter.ModelChoiceFilter(
        label = 'Kategoria',
        field_name = 'kategoriaID',
        to_field_name = 'id',
        queryset = Kategoria.objects.all(),
        widget = forms.Select(attrs = {'class' : 'form-control'}) 
    )

    class Meta:
        model = Teszt
        fields = ['kategoriaID']