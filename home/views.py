from django.shortcuts import render, redirect
# from django.http import HttpResponse
from posts.models import Post, Comment
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    posts = Post.objects.all()
    # comments from current user
    comments = Comment.objects.all()
    
    post_comments = {post.id: [] for post in posts}
    for comment in comments:
        post_comments[comment.post_id].append(comment)
    
    context_data = {
        'user': request.user,
        'posts': posts,
        'post_comments': post_comments
    }
    return render(request, 'home.html', context_data)

def user_logout(request):
    logout(request)
    return redirect('index')

class UserLogin(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class UserProfile(generic.DetailView):
    template_name = 'user_profile.html'
    model = User
    context_object_name = 'profile_user'

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(owner=user)
        context['comments'] = Comment.objects.filter(post__owner=user)
        return context