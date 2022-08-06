from django import forms
from .models import DisasterName


class FormDisaster(forms.ModelForm):
    class Meta:
        model = DisasterName
        fields = '__all__'
        # widgets = {
        #     'name': forms.CharField(widget=forms.TextInput)
        # }