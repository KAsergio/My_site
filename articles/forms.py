#Ne sais pas encore l'utilité de cette ligne de code. SI utilité trouvé, révisualiser le cours 187 et 188.

from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title' , 'contain', 'slug', 'theme', 'image']