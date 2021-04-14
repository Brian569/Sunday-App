from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['name', 'my_picture', 'about', 'email', 'phone_number']
        exclude = ['user', 'my_posts']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content', 'article_link']
        exclude = ['posted_by']