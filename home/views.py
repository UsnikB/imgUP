from django.shortcuts import render, redirect
# from django.http import HttpResponse
from posts.models import Post, Comment
from django.contrib.auth import logout

# Create your views here.
def index(request):
    posts = Post.objects.all()
    # comments from current user
    comments = Comment.objects.all()
    
    context_data = {
        'user': request.user,
        'posts': posts,
        'comments': comments
    }
    return render(request, 'home.html', context_data)

def user_logout(request):
    logout(request)
    return redirect('index')