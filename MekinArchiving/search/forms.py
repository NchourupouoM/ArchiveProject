from django import forms

class SearchForm(forms.Form):
    rechercher = forms.TextInput(max_length=1000,label="Rechercher")