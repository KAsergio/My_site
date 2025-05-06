from django.contrib import admin
from .models import OpenSourceProject, Technology

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(OpenSourceProject)
class OpenSourceProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'date_created')
    list_filter = ('category', 'status', 'technologies')
    search_fields = ('title', 'description')
    filter_horizontal = ('technologies',)
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'image')
        }),
        ('Catégorisation', {
            'fields': ('category', 'status', 'technologies')
        }),
        ('Liens', {
            'fields': ('github_link', 'drive_link')
        }),
    )
