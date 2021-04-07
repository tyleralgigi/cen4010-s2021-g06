from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from post.models import Post


@login_required
def index(request):
    posts = Post.objects.all().order_by('timestamp')
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page
    }

    return render(request, 'feed.html', context)
