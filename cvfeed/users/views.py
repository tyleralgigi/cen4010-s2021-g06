from django.shortcuts import render
from .forms import RegisterForm


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

