from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Article, Comment

def articles_list_view(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'articles/articles_list.html', context={'articles': articles})


def article_view(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == "POST":
        comment_content = request.POST.get("comment")
        if comment_content:
            Comment.objects.create(
                article=article,
                author=request.user.username if request.user.is_authenticated else "Anonyme",
                content=comment_content,
            )
        return redirect("articles:article", slug=slug)  # Redirige pour éviter le double POST

    comments = article.comments.all()  # Récupérer les commentaires
    return render(request, 'articles/article_page.html', {'article': article, 'comments': comments})
    


#try :
        #article = Article.objects.get(slug=slug)
        #return render (request, 'articles/article_page.html', context={"articles": article})
    #except Article.DoesNotExist :
        #raise Http404("L'article n'existe pas")
    