from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.utils.html import escape

from .models import Produit, Terms, Profil, Commande


def index(request):
    context = {}
    context["produits"] = Produit.objects.order_by("name")
    context["profils"] = Profil.objects.order_by("slug")
    return render(request, 'index.html', context=context)


def get_page_produit(request, slug):
    context = {}
    context["produit"] = Produit.objects.get(slug=slug)
    context["produits"] = Produit.objects.order_by("name")
    return render(request, 'product.html', context=context)


def terms_of_use(request):
    context = {}
    context["content"] = Terms.objects.get()
    context["produits"] = Produit.objects.order_by("name")
    return render(request, 'condition_of_use.html', context=context)


def get_page_commande(request, slug):
    context = {}
    context["produit"] = Produit.objects.get(slug=slug)
    context["produits"] = Produit.objects.order_by("name")
    return render(request, 'commande.html', context=context)

def commande(request):
    if request.POST:
        context = {}
        username = escape(request.POST.get("name"))
        product_name = escape(request.POST.get("product_name"))
        email = escape(request.POST.get("email"))
        description = escape(request.POST.get("message"))
        tel = escape(request.POST.get("phone"))
        commande_, _ = Commande.objects.get_or_create(username=username, product_name= product_name, tel=tel, email_user=email,
                                                      description=description, slug=slugify(username))
        context["contacter"] = commande_
        return render(request, 'vide.html', context=context)
    return render(request, 'services/devis.html')