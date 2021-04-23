from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

from post.models import Post
from .forms import RegisterForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/register.html', context={'form': form})

    return render(request, 'registration/register.html')
