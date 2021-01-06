from django import forms
from .models import URL
from django.contrib.auth.forms import UserCreationForm

class LinkGenerateForm(forms.ModelForm):
    long_url = forms.URLField(max_length=2048, label="")

    class Meta:
        model = URL
        fields = [
            'long_url',
        ]

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)