from django import forms
from django.forms import widgets
from webapp.models import status_choices


class BookForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Автор', empty_value="Unknown")
    email = forms.EmailField(max_length=100, required=True, label='E-mail')
    text = forms.CharField(max_length=3000, required=True, label='Текст статьи', widget=widgets.Textarea)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=40, required=True, label='', widget=widgets.TextInput)
    # search = forms.Form()
