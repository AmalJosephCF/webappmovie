from django import forms
from django.contrib.auth.models import User

from movieapp.models import Movie


class movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','cast','trailer','rel_date','image','category']

