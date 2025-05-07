from django.db import models
from django.contrib.auth.models import User
from core.models import Category


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default_project.jpg', upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[
        ('in_progress', 'En cours'),
        ('completed', 'Terminé'),
        ('on_hold', 'En attente')
    ], default='completed')
    featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True, related_name='projects')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']
