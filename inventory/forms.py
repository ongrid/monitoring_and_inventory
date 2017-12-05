from django import forms

from .models import *

class PartForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ('type', 'part','serial', 'broken', 'comment')