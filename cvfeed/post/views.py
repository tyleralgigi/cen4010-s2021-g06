from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def new_post(request):
    if request.method == 'POST':
        print('post')
    return render(request, 'post.html')
