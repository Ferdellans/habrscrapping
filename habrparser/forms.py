from django import forms


class ParserForm(forms.Form):
    url = forms.URLField(label='url')
    file = forms.FileField(label='file')
