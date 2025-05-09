from django.contrib import admin
from .models import Category, CarouselImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description']
    list_editable = ['description']

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at', 'image_preview')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    ordering = ('order', '-created_at')
    readonly_fields = ('created_at', 'image_preview')
    fieldsets = (
        ('Informations', {
            'fields': ('title', 'image', 'image_preview')
        }),
        ('Configuration', {
            'fields': ('order', 'is_active', 'created_at')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px;"/>'
        return "Aucune image"
    image_preview.short_description = 'Aperçu'
    image_preview.allow_tags = True
