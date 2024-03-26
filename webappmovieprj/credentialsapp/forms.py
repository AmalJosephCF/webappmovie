from django import forms
from django.contrib.auth.models import User

from movieapp.models import Movie


class userForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

