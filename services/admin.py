from django.contrib import admin
from .models import Produit, Terms, Profil, Commande

# Register your models here.

admin.site.register(Produit)
admin.site.register(Terms)
admin.site.register(Profil)
admin.site.register(Commande)