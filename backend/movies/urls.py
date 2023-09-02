from django.urls import path
from . import views

urlpatterns = [
    path('', views.popular, name="index"),
    path('<int:movie_id>/', views.detail, name="detail"),
    path('search/', views.search, name="search"),
    path('popular/', views.popular, name="popular"),
    path('upcoming/', views.upcoming, name="upcoming"),
    path('trailer/<int:movie_id>/', views.movie_trailer, name="trailer"),
    path('genre/', views.genre, name="genre"),
    path('genre/movies/', views.genreMovies, name="genre_moveis"),
    path('recommend/',views.recommend, name="recommend"),
    # path('login/',views.loginPage, name="login"),
]