from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm

# In accounts/views.py
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to 'home' after registration
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to 'home' after login
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('home')


def home(request):
    if request.user.is_authenticated:
        return redirect('webfeed')  # Redirect authenticated users to the webfeed
    else:
        return redirect('login')  # Redirect unauthenticated users to the login page

from .forms import PostForm
from .models import Post, Like

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('webfeed')
    else:
        form = PostForm()
    return render(request, 'accounts/create_post.html', {'form': form})

def webfeed(request):
    posts = Post.objects.all().order_by('-created_at')  # Get all posts, ordered by latest first
    return render(request, 'accounts/webfeed.html', {'posts': posts})

from django.http import JsonResponse

def like_post(request, post_id):
    if request.method == 'POST' and request.user.is_authenticated:
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()  # Unlike if already liked
        return JsonResponse({'likes_count': post.like_set.count()})
    return JsonResponse({'error': 'Invalid request'}, status=400)