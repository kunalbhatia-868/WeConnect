from django import forms
from main import models

class PostForm(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=('content','image')