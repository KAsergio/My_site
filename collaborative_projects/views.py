from django.shortcuts import render, get_object_or_404
from .models import OpenSourceProject

# Create your views here.

def opensource_list_view(request):
    # Récupérer la catégorie sélectionnée
    current_category = request.GET.get('category')
    
    # Récupérer tous les projets
    projects = OpenSourceProject.objects.all()
    
    # Filtrer par catégorie si une catégorie est sélectionnée
    if current_category:
        projects = projects.filter(category=current_category)
    
    # Récupérer toutes les catégories uniques
    categories = OpenSourceProject.objects.values_list('category', flat=True).distinct()
    
    context = {
        'projects': projects,
        'categories': categories,
        'current_category': current_category,
    }
    
    return render(request, 'opensource.html', context)

def opensource_detail_view(request, pk):
    project = get_object_or_404(OpenSourceProject, pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'opensource_detail.html', context)
