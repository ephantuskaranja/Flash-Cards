from django import forms
from .models import Flshcard

class NoteForm(forms.Form):
    class Meta:
        model = Flshcard
        exclude = ['user','course']