from django.urls import path, re_path
from .views import (
    home, profile, update_profile,
    logout_view, posts, add_article
)

urlpatterns = [
    path('', home, name = 'home'),
    re_path(r'profile/(\d+)', profile, name = 'profile'),
    path('update_profile/', update_profile, name = 'update_profile'),
    path('logut/', logout_view, name = 'logouts'),
    path('posts/', posts, name ='posts'),
    path('add_article/', add_article, name = 'add_article'),
]