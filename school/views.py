from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}

    return render(request, 'home.html', context)

@login_required
def profile(request, id):
    user = User.objects.filter(pk = id)
    profile = TeacherProfile.objects.filter(user=id)

    context = {'profile': profile}

    return render(request, 'my_accounts/profile.html', context)

@login_required
def update_profile(request):
    current_user = request.user

    if request.method  == 'POST':
        if TeacherProfile.objects.filter(user_id = current_user).exists():
            form = ProfileForm(request.POST, request.FILES, instance= TeacherProfile.objects.get(user_id = current_user))

        else:
            form = ProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = current_user
            prof.save()

            message = 'Profile updated succesfully'
            return redirect('profile', current_user.id)

        
    else:
        if TeacherProfile.objects.filter(user_id = current_user).exists():
            form = ProfileForm(instance = TeacherProfile.objects.get(user_id = current_user))
        else:
            form = ProfileForm()

    return render(request, 'my_accounts/update_profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')