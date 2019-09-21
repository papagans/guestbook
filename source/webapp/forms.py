from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Заголовок')
    text = forms.CharField(max_length=3000, required=True, label='Текст статьи', widget=widgets.Textarea)
    author = forms.CharField(max_length=40, required=False, label='Автор', empty_value="Unknown")
