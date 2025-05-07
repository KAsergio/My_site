from django.contrib import admin

from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    autocomplete_fields = ['categories']

admin.site.register(Comment)
