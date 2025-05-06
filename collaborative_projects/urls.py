from django.urls import path
from . import views

urlpatterns = [
    path('', views.opensource_list_view, name='opensource_list'),
    path('<int:pk>/', views.opensource_detail_view, name='opensource_detail'),
] 