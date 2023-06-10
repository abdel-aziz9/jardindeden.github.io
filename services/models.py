from django.db import models
from django.utils.text import slugify


class Terms(models.Model):
    content = models.TextField()


class Article(models.Model):
    titre = models.CharField(max_length=150, unique=True, verbose_name='Titre')
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    image = models.ImageField(upload_to='image_article')
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(default='')

    def as_default(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre


class Actu(models.Model):
    titre = models.CharField(max_length=150, unique=True, verbose_name='Titre')
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    image = models.ImageField(upload_to='image_article')
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(default='')

    def as_default(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre
