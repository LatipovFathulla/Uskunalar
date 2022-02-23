from django import forms

from about.models import RequestsModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = RequestsModel
        exclude = ['created_at']