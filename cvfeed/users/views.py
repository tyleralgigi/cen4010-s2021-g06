from django.shortcuts import render

from post.models import Post
from .forms import RegisterForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
        else:
            return render(request, 'registration/register.html', context={'form': form})

    return render(request, 'registration/register.html')


def user_view(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    print(posts)

    context = {
        'viewedUser': user,
        'posts': posts
    }

    return render(request, 'user_view.html', context)
