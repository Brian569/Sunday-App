from django.urls import path, re_path
from .views import (
    student_home, my_posts,
    choice, single_post,
    all_teachers
)

urlpatterns = [
    path('', choice, name = 'choice'),
    path('all_teachers/', all_teachers, name = 'all_teachers'),
    path('student_home/', student_home, name = 'student_home'),
    path('my_posts/', my_posts , name = 'new_posts'),
    re_path(r'my_singlepost/(\d+)', single_post, name = "my_singlepost")
]