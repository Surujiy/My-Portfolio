from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatMainView.as_view(), name='all'),
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('lookup/', views.BreedView.as_view(), name='breed_list'),
    path('CatLookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('CatLookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('CatLookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]