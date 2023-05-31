from django import forms
from django.forms import ModelForm, ValidationError
from .models import *



class tesztForm(ModelForm):
    class Meta:
        model = Teszt
        fields = "__all__"
        widgets = {
            "kerdes" : forms.TextInput(attrs = {"class" : "form-control"}),
            "v1" : forms.TextInput(attrs = {"class" : "form-control"}),
            "v2" : forms.TextInput(attrs = {"class" : "form-control"}),
            "v3" : forms.TextInput(attrs = {"class" : "form-control"}),
            "v4" : forms.TextInput(attrs = {"class" : "form-control"}),
            "kategoriaID" : forms.Select(attrs = {"class" : "form-control"})
        }


