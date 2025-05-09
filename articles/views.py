from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings
from .models import Article, Comment, Category
from core.views import get_carousel_images

def articles_list_view(request):
    current_category = request.GET.get('category')
    articles = Article.objects.all().order_by('-publication_date')
    if current_category:
        articles = articles.filter(categories__name=current_category)
    categories = Category.objects.values_list('name', flat=True).distinct()
    return render(request, 'articles/articles_list.html', context={
        'articles': articles,
        'categories': categories,
        'current_category': current_category,
    })


def article_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.views_count += 1
    article.save(update_fields=['views_count'])

    if request.method == "POST":
        comment_content = request.POST.get("comment")
        if comment_content:
            parent_id = request.POST.get("parent_id")
            parent = None
            if parent_id:
                parent = Comment.objects.get(id=parent_id)
            
            Comment.objects.create(
                article=article,
                author=request.user.username if request.user.is_authenticated else request.POST.get("author", "Anonyme"),
                content=comment_content,
                contact=request.POST.get("contact", ""),
                parent=parent
            )
        return redirect("articles:article", slug=slug)

    comments = article.comments.filter(parent=None)  # Récupérer uniquement les commentaires parents
    return render(request, 'articles/article_page.html', {'article': article, 'comments': comments})
    


#try :
        #article = Article.objects.get(slug=slug)
        #return render (request, 'articles/article_page.html', context={"articles": article})
    #except Article.DoesNotExist :
        #raise Http404("L'article n'existe pas")
    
def home(request):
    articles = Article.objects.all().order_by('-publication_date')
    carousel_images = get_carousel_images()
    return render(request, 'articles/home.html', {
        'articles': articles,
        'carousel_images': carousel_images,
        'debug': settings.DEBUG
    })
    