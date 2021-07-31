from django.forms import ValidationError
from django import forms
from .models import Voters
class VoterForms(forms.ModelForm):

    class Meta:
        model=Voters
        fields='__all__'

    def clean(self):
        user_clean_data=super().clean()
        age=user_clean_data['age']
        if int(age)<18:
            raise ValidationError("You are not eligible for voting")

class Delete(forms.Form):
    name=forms.CharField(widget=forms.TextInput,max_length=30,min_length=3)
    email=forms.EmailField(widget=forms.EmailInput)


class Updates(forms.ModelForm):
    class Meta:
        model=Voters
        fields='__all__'


