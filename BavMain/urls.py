from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from BavMain import settings
from services import views
from services.views import article_post, article_actu

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path("politique-de-confidentialite/", views.terms_of_use, name='terms_of_use'),
    path('article-post/<str:slug>/', article_post, name='article'),
    path('article-actu/<str:slug>/', article_actu, name='actu'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
