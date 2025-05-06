from django.db import models
from django.contrib.auth.models import User


class Article (models.Model):
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types

    title = models.CharField(max_length = 150)
    contain = models.TextField()
    slug = models.SlugField(max_length = 100)
    publication_date = models.DateTimeField(auto_now_add=True)
    theme = models.TextField()
    image = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.title



class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"