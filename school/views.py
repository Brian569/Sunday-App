from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}

    return render(request, 'home.html', context)

    
@login_required
def posts(request):

    articles = Article.objects.all().order_by('-id')

    return render(request, 'post.html', {'articles' : articles})

   
@login_required
def profile(request, id):
    user = User.objects.filter(pk = id)
    profile = TeacherProfile.objects.filter(user=id)
    article = Article.objects.filter(posted_by=id)

    context = {'profile': profile, 'article' : article}

    return render(request, 'my_accounts/profile.html', context)

@login_required
def update_profile(request):
    current_user = request.user

    if request.method  == 'POST':
        if TeacherProfile.objects.filter(user_id = current_user).exists():
            form = ProfileForm(request.POST, request.FILES, instance= TeacherProfile.objects.get(user_id = current_user))
            prof = TeacherProfile.objects.filter(user_id = current_user)
        else:
            form = ProfileForm(request.POST, request.FILES)
            prof = TeacherProfile.objects.filter(user_id = current_user)
        
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = current_user
            prof.save()

            message = 'Profile updated succesfully'
            return redirect('profile', current_user.id)

        
    else:
        if TeacherProfile.objects.filter(user_id = current_user).exists():
            form = ProfileForm(instance = TeacherProfile.objects.get(user_id = current_user))
            prof = TeacherProfile.objects.filter(user_id = current_user)
        else:
            form = ProfileForm()
            prof = TeacherProfile.objects.filter(user_id = current_user)

    return render(request, 'my_accounts/update_profile.html', {'form': form, 'prof': prof})


@login_required
def add_article(request):
    current_user = request.user

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.posted_by = current_user
            article.save() 

            messo = 'article posted successfully!'
            return redirect('posts')
    
    else:
        form = ArticleForm()

    return render(request, 'add_article.html', {'form': form})


def logout_view(request):

    logout(request)

    return redirect('login')

def single_post(request, post_id):
  
    post = Article.objects.filter(pk=post_id)

    return render(request, 'single_post.html', {"post": post})