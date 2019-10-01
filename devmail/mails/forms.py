from django import forms

class SearchForm(forms.Form):

    subject = forms.CharField(max_length=150)

    def clean(self):
        all_clean_data = super().clean()
        subject = all_clean_data['subject']
