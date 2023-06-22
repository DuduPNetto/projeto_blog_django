from blog import models
from django.core.paginator import Paginator
from django.shortcuts import render

PER_PAGE = 9

def index(request):
    posts = models.Post.objects.get_published()

    paginator = Paginator(posts, per_page=PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def created_by(request, author_pk):
    posts = models.Post.objects.get_published().filter(created_by__pk=author_pk)

    paginator = Paginator(posts, per_page=PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def category(request, slug):
    posts = models.Post.objects.get_published().filter(category__slug=slug)

    paginator = Paginator(posts, per_page=PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def tag(request, slug):
    posts = models.Post.objects.get_published().filter(tags__slug=slug)

    paginator = Paginator(posts, per_page=PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def page(request, slug):
    return render(
        request,
        'blog/pages/page.html'
    )

def post(request, slug):
    post = models.Post.objects.get_published().filter(slug=slug).first()

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post
        }
    )