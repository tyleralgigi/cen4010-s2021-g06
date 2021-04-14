from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone

from users.models import User
from feed.forms import SearchForm, ReportForm, RemovePostForm
from post.models import Post, Report


@login_required
def index_feed(request):
    posts = Post.objects.filter(is_hidden=False)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page
    }

    return render(request, 'feed_base.html', context)


@login_required
def user_feed(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404(username + ' does not exist!')
    posts = Post.objects.filter(author=user, is_hidden=False)

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'viewedUser': user,
        'page': page
    }

    return render(request, 'feed_user.html', context)


@login_required
def tag_feed(request, tag):
    if not tag.startswith('#'):
        tag = '#' + tag

    posts = Post.objects.filter(description__contains=tag, is_hidden=False)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'tag': tag,
        'page': page
    }

    return render(request, 'feed_tag.html', context)


@login_required
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            if 'user_search' in form.data:
                return redirect('/user/' + form.cleaned_data.get('search_text') + '/')
            if 'tag_search' in form.data:
                return redirect('/tag/' + form.cleaned_data.get('search_text') + '/')

    return redirect('/')


@login_required
@staff_member_required
def reports_feed(request):
    reported_post_ids = Report.objects.order_by('-timestamp').values_list('post').distinct()
    reported_posts = Post.objects.filter(id__in=reported_post_ids)

    reports = list()

    for p in reported_posts:
        reports.append({
            'post': p,
            'reports': Report.objects.filter(post=p)
        })

    paginator = Paginator(reports, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page
    }

    return render(request, 'feed_reports.html', context)


@login_required
@staff_member_required
def remove_post(request):
    if request.method == 'POST':
        form = RemovePostForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(id=form.cleaned_data.get('post_id'))
            post.is_hidden = True
            post.save()

            reports = Report.objects.filter(post=post)

            for r in reports:
                r.delete()

    return redirect('/reports/')


@login_required
def report_post(request, post_id):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            r = Report(
                post=Post.objects.get(id=post_id),
                reporter=request.user,
                report_description=form.cleaned_data.get('report_description'),
                timestamp=timezone.now(),
            )
            r.save()
            return render(request, 'generic.html', context={'message': 'Your report has been received!'})
    return redirect('/')
