from django.shortcuts import render
from school.models import Article


def choice(request):

    return render(request, 'choice.html')

    
def student_home(request):
   
    return render(request, 'student_home.html')

def my_posts(request):

    articles = Article.objects.all()

    return render(request, 'my_posts.html', {'articles' : articles})