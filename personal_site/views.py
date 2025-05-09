from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from projects.models import Project
from articles.models import Article
from core.views import get_carousel_images

def home_view(request):
    # Récupérer les 3 projets mis en avant les plus récents
    featured_projects = Project.objects.filter(featured=True).order_by('-date_created')[:3]
    # Récupérer les articles récents
    articles = Article.objects.all().order_by('-publication_date')
    # Récupérer les images du carrousel
    carousel_images = get_carousel_images()
    
    return render(request, 'home.html', {
        'featured_projects': featured_projects,
        'articles': articles,
        'carousel_images': carousel_images,
        'debug': settings.DEBUG
    })

def service_view(request):
    return render(request,'opensource.html')

def project_view(request):
    # Rediriger vers la nouvelle URL de projets
    return redirect('projects:projects')

def publication_view(request):
    return render(request,'publication.html')

def contact_view(request):
    form = ContactForm()
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            title = f'Site | Contact de {name} ({email})'
            email_message = f"Nom : {name}\nE-mail : {email}\nTéléphone : {phone}\n\nMessage :\n{message}"

            try:
                send_mail(
                    title,
                    email_message,
                    'contact@sergioassogba.com',
                    ['contact@sergioassogba.com'],
                    fail_silently=False,
                )
                success = True
            except Exception as e:
                form.add_error(None, f"Une erreur s'est produite lors de l'envoi de l'e-mail : {e}")

    return render(request, 'contact.html', {"form": form, "success": success})

def cursus_view(request):
    return render(request,'cursus.html')

def remerciements_view(request):
    return HttpResponse("Merci de nous avoir contacter")