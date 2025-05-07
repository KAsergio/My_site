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

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"