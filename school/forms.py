from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['name', 'my_picture', 'about', 'phone_number']
        exclude = ['user', 'my_posts', 'email']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['posted_by']