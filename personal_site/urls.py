from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('articles/', include('articles.urls')),
    path('projects/', include('projects.urls')),
    path('collaborative-projects/', include('collaborative_projects.urls')),
    path('contact/', views.contact_view, name='contact'),
    path('remerciements/', views.remerciements_view, name='remerciements'),
    path('cursus/', views.cursus_view, name='cursus'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
