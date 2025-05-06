from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'content', 'slug', 'image', 'category', 
                 'github_link', 'live_link', 'technologies', 'status', 'featured'] 