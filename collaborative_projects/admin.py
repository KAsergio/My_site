from django.contrib import admin
from .models import OpenSourceProject, Technology

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(OpenSourceProject)
class OpenSourceProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_created')
    list_filter = ('status', 'technologies')
    search_fields = ('title', 'description')
    filter_horizontal = ('technologies',)
    autocomplete_fields = ['categories']
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'image')
        }),
        ('Catégorisation', {
            'fields': ('status', 'technologies', 'categories')
        }),
        ('Liens', {
            'fields': ('github_link', 'drive_link')
        }),
    )
