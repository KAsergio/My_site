from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Project

def projects_list_view(request):
    """Vue pour afficher la liste de tous les projets"""
    # Par défaut, on affiche tous les projets triés par date de création
    projects = Project.objects.all()
    
    # Filtrage par catégorie si spécifié dans l'URL
    category = request.GET.get('category')
    if category:
        projects = projects.filter(category=category)
    
    # Récupération de toutes les catégories pour le filtre
    categories = Project.objects.values_list('category', flat=True).distinct()
    
    context = {
        'projects': projects,
        'categories': categories,
        'current_category': category
    }
    
    return render(request, 'projects/projects_list.html', context)

def project_detail_view(request, slug):
    """Vue pour afficher les détails d'un projet spécifique"""
    project = get_object_or_404(Project, slug=slug)
    
    # Projets similaires (même catégorie, excluant le projet actuel)
    similar_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'similar_projects': similar_projects
    }
    
    return render(request, 'projects/project_detail.html', context)
