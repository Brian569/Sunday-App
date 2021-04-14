from django.urls import path, re_path
from .views import (
    student_home, my_posts,
    choice
)

urlpatterns = [
    path('', choice, name = 'choice'),
    path('student_home/', student_home, name = 'student_home'),
    path('my_posts/', my_posts , name = 'new_posts'),
]