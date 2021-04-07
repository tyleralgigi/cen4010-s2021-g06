from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from post.forms import PostForm, CommentForm
from post.models import Post, Comment


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = Post(
                author=request.user,
                timestamp=timezone.now(),
                description=form.cleaned_data.get('description'),
                image=form.cleaned_data.get('image')
            )
            obj.save()

            return redirect('/post/%d/' % obj.id)

    context = dict()
    context['form'] = PostForm()

    return render(request, 'new_post.html', context)


@login_required
def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = Comment(
                author=request.user,
                post=post,
                comment=form.cleaned_data.get('comment'),
                timestamp=timezone.now(),
            )
            obj.save()

    comments = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'comments': comments
    }

    return render(request, 'post.html', context)
