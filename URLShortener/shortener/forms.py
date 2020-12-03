from django import forms
from .models import URL

class LinkGenerateForm(forms.ModelForm):
    long_url = forms.URLField(max_length=2048, label="Full URL")

    class Meta:
        model = URL
        fields = [
            'long_url',
        ]
