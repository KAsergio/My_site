from django.contrib import admin

from .models import Article, Comment, CarouselImage

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    autocomplete_fields = ['categories']

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('order', '-created_at')
    fieldsets = (
        ('Informations', {
            'fields': ('title', 'image')
        }),
        ('Configuration', {
            'fields': ('order', 'is_active')
        }),
    )

admin.site.register(Comment)
