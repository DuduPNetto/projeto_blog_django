from blog import models
from django.core.paginator import Paginator
from django.db.models import Q
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

def search(request):
    search_value = request.GET.get('search', '').strip()
    posts = models.Post.objects.get_published().filter(
        Q(title__icontains=search_value) |
        Q(excerpt__icontains=search_value) |
        Q(content__icontains=search_value)
    )[:PER_PAGE]

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
            'search_value': search_value
        }
    )

def page(request, slug):
    page = models.Page.objects.filter(is_published=True).filter(slug=slug).first()

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page
        }
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