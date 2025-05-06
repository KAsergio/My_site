from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path('', views.projects_list_view, name='projects'),
    path('<slug:slug>/', views.project_detail_view, name='project'),
]
