from django.db import models
from django.contrib.auth.models import User
from core.models import Category


class Article (models.Model):
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types

    title = models.CharField(max_length = 150)
    contain = models.TextField()
    slug = models.SlugField(max_length = 100)
    publication_date = models.DateTimeField(auto_now_add=True)
    theme = models.TextField()
    image = models.ImageField(default='default.jpg')
    views_count = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True, related_name='articles')

    def __str__(self):
        return self.title



class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    contact = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"

    class Meta:
        ordering = ['date_posted']


class CarouselImage(models.Model):
    title = models.CharField(max_length=100, help_text="Titre de l'image")
    image = models.ImageField(upload_to='carousel/', help_text="Image du carrousel")
    order = models.PositiveIntegerField(default=0, help_text="Ordre d'affichage")
    is_active = models.BooleanField(default=True, help_text="Afficher cette image dans le carrousel")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Image du carrousel"
        verbose_name_plural = "Images du carrousel"

    def __str__(self):
        return self.title