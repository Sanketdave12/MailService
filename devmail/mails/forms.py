from django import forms
from . import models
from searchableselect.widgets import SearchableSelect
from account.models import User

class ComposeForm(forms.ModelForm):

    class Meta:
        fields = ('receiver', 'subject', 'message')
        model = models.Mails
        labels = {
            'receiver' : 'To',
        }
        widgets = {
            'receiver': forms.Select(attrs={
                'class' : 'selectpicker',
                'data-live-search' : 'true',
                'data-size' : '5',
                'required' : 'required'
            }),
            'subject': forms.TextInput(),
        }
