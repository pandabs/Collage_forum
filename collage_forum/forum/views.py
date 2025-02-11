from django.shortcuts import render,get_object_or_404,redirect
from .models import Forum
from .forms import ForumForm,CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import Forum, Comment
from django.http import JsonResponse
 


def index(request):
    return render(request, 'forum/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'register.html', {'error': 'Email already exists'})
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('forum')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('forum')
    return render(request, 'login.html')

def edit_forum(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.user != forum.user:
        return JsonResponse({'error': 'You are not authorized to edit this post.'}, status=403)
    
    if request.method == 'POST':
        form = ForumForm(request.POST, instance=forum)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = ForumForm(instance=forum)
    
    # Render only the form for AJAX requests
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'partials/edit_form.html', {'form': form})
    
    return render(request, 'edit_forum.html', {'form': form})

def delete_forum(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.user == forum.user:
        forum.delete()
    return redirect('forum')

def add_comment(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.forum = forum
            comment.save()
            return redirect('forum_detail', forum_id=forum.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

def contactus(request):
    return render(request, 'contactus.html')

def forum(request):
    return render(request, 'forum.html')

def forum_view(request):
    forums = Forum.objects.all().order_by('-created_at')
    return render(request, 'forum.html', {'forums': forums})

def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    return render(request, 'forum_detail.html', {'forum': forum})

def create_forum(request):
    return render(request, 'create_forum.html')

def logout_view(request):
    logout(request)
    return redirect('/')