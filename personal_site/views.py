from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail

from .forms import ContactForm

# Importer le modèle Project
from projects.models import Project

def home_view(request):
    # Récupérer les 3 projets mis en avant les plus récents
    featured_projects = Project.objects.filter(featured=True).order_by('-date_created')[:3]
    return render(request, 'home.html', {'featured_projects': featured_projects})

def service_view(request):
    return render(request,'opensource.html')

def project_view(request):
    # Rediriger vers la nouvelle URL de projets
    return redirect('projects:projects')

def publication_view(request):
    return render(request,'publication.html')

'''def contact_view(request): 
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Titre et contenu de l'e-mail
            title = f'Site | Contact de {name} ({email})'
            email_message = f"Nom : {name}\nE-mail : {email}\nTéléphone : {phone}\n\nMessage :\n{message}"

            try:
                # Envoi de l'e-mail
                send_mail(
                    title, 
                    email_message, 
                    'contact@sergioassogba.com',  # Adresse de l'expéditeur
                    ['contact@sergioassogba.com'],  # Liste des destinataires
                    fail_silently=False,  # Afficher les erreurs en cas de problème
                )
                return HttpResponseRedirect(reverse('remerciements'))  # Redirection après succès
            except Exception as e:
                # Ajoutez un message d'erreur ou gérez l'exception
                form.add_error(None, f"Une erreur s'est produite lors de l'envoi de l'e-mail : {e}")

    return render(request, 'contact.html', {"form": form})

'''
def contact_view(request):
    form = ContactForm()
    success = False  # Initialisez le drapeau de succès

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
                success = True  # Le formulaire a été soumis avec succès
            except Exception as e:
                form.add_error(None, f"Une erreur s'est produite lors de l'envoi de l'e-mail : {e}")

    return render(request, 'contact.html', {"form": form, "success": success})




def cursus_view(request):
    return render(request,'cursus.html')

def remerciements_view(request):
    return HttpResponse("Merci de nous avoir contacter")