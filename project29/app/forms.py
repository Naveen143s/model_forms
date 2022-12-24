from django import forms
from app.models import *

class ModelForms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForms(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class AcessRecordsForms(forms.ModelForm):
    class Meta:
        model=Acessrecords
        fields='__all__'
   