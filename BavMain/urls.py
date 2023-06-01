from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from BavMain import settings
from services import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('produit/<str:slug>/', views.get_page_produit, name='produit'),
    path("politique-de-confidentialite/", views.terms_of_use, name='terms_of_use'),
    path('page_commande/<str:slug>/', views.get_page_commande, name='page_commande'),
    path('commande', views.commande, name='commande'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
