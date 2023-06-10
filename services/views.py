from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.utils.html import escape

from .models import Terms, Article, Actu


def index(request):
    context = {}
    context["posts"] = Article.objects.filter(published=True)
    context["actu"] = Actu.objects.filter(published=True)
    return render(request, 'index.html', context=context)


def terms_of_use(request):
    context = {}
    context["content"] = Terms.objects.get()
    return render(request, 'condition_of_use.html', context=context)


def article_post(request, slug):
    context = {}
    post = Article.objects.get(slug=slug)
    context["article"] = post
    return render(request, 'article_blog.html', context=context)


def article_actu(request, slug):
    context = {}
    post = Actu.objects.get(slug=slug)
    context["actu"] = post
    return render(request, 'article_actu.html', context=context)