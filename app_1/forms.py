from django import forms
from .models import App


class PostForm(forms.ModelForm):
    class Meta:
        model = App
        fields = '__all__'