from django import forms

from about.models import RequestsModel


class RequestModelForm (forms. ModelForm):
    class Meta:
        model = RequestsModel
        exclude = ['created_at']
