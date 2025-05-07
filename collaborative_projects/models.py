from django.db import models
from django.utils import timezone
from core.models import Category

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Technologies"

class OpenSourceProject(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Terminé'),
        ('in_progress', 'En cours'),
        ('planned', 'Planifié'),
    ]

    CATEGORY_CHOICES = [
        ('web', 'Développement Web'),
        ('data', 'Data Science'),
        ('energy', 'Énergétique'),
        ('other', 'Autre'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='opensource/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    technologies = models.ManyToManyField(Technology, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    github_link = models.URLField(blank=True, null=True)
    drive_link = models.URLField(blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True, related_name='opensource_projects')

    def __str__(self):
        return self.title

    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])

    class Meta:
        verbose_name = "Projet Open Source"
        verbose_name_plural = "Projets Open Source"
        ordering = ['-date_created']
