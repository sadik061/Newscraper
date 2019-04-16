from django import forms


class customform(forms.Form):
    link = forms.CharField()
    key = forms.CharField()