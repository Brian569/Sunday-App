from django.shortcuts import render
from school.models import Article, TeacherProfile


def choice(request):

    return render(request, 'choice.html')

    
def student_home(request):
   
    return render(request, 'student_home.html')

def my_posts(request):

    articles = Article.objects.all().order_by('-id')

    return render(request, 'my_posts.html', {'articles' : articles})

def single_post(request, post_id):
  
    post = Article.objects.filter(pk=post_id).order_by('-id')

    return render(request, 'my_singlepost.html', {"post": post})

def all_teachers(request):

    teachers = TeacherProfile.objects.all().order_by('-id')

    return render(request, 'all_teachers.html', {'teachers': teachers})