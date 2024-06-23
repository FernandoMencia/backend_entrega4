from django.contrib import admin
from django.urls import path, include

from .views import (
    DirectorListView,
    DirectorDetailView,
    MovieListView,
    MovieDetailView,
    movies_by_director,
    DirectorUpdateView, 
    DirectorDeleteView,
    MovieUpdateView, 
    MovieDeleteView
)

urlpatterns = [
    # Rutas para vistas basadas en clases
    path('directors/', DirectorListView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    
    # Ruta personalizada para obtener películas de un director específico
    path('directors/<int:director_id>/movies/', movies_by_director, name='movies-by-director'),
    
    #Rutas vistas genéricas añadidas
    path('directors/<int:pk>/update/', DirectorUpdateView.as_view(), name='director-update'),
    path('directors/<int:pk>/delete/', DirectorDeleteView.as_view(), name='director-delete'),
    path('movies/<int:pk>/update/', MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),
]

