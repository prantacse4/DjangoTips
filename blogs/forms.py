from django.core import validators
from django import forms
from .models import Post
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    coverimage = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = ['user', 'topic', 'blog', 'coverimage']
