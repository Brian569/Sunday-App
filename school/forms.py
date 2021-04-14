from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['name', 'my_picture', 'about', 'email', 'phone_number']
        exclude = ['user']

class ArticleForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'image', 'content']
        exclude = ['posted_by']