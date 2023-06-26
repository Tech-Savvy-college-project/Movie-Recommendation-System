from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_data),
    path('<int:id>/', views.movie_detail),
    path('search/', views.search),
    path('popular/', views.popular),
    path('genre/', views.genre),
    path('genre/movies/', views.genreMovies),

]