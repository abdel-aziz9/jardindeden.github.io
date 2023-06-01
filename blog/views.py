from django.shortcuts import render
from .models import Article
from services.models import Produit


def BlogHome(request):
    context = {}
    context["posts"] = Article.objects.filter(published=True)
    context["services"] = Produit.objects.order_by('name')
    return render(request, 'blog/blog.html', context=context)


def article_post(request, slug):
    context = {}
    post = Article.objects.get(slug=slug)
    context["article"] = post
    context["services"] = Produit.objects.order_by('name')
    return render(request, 'blog/article_blog.html', context=context)
