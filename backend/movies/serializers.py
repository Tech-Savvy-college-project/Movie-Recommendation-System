import jmespath
import requests
import json

from rest_framework import serializers
from .models import Movie
from .utils import *

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['tmdb_id', 'imdb_id', 'original_language', 'original_title', 'title', 'runtime_', 'genre', 'poster', 'overview', 'tagline', 'prod_company', 'release_date', 'spoken_language']
  
    title = serializers.SerializerMethodField(method_name='get_title')
    genre = serializers.SerializerMethodField(method_name='get_genre')    
    poster = serializers.SerializerMethodField(method_name='get_poster')
    overview = serializers.SerializerMethodField(method_name='get_overview')
    tagline = serializers.SerializerMethodField(method_name='get_tagline')
    prod_company = serializers.SerializerMethodField(method_name='get_production_company')
    release_date = serializers.SerializerMethodField(method_name='get_release_date')
    spoken_language = serializers.SerializerMethodField(method_name='get_spoken_language')
    runtime_ = serializers.SerializerMethodField(method_name='get_runtime')

    def get_runtime(self, movie: Movie):
        return f"{movie.runtime} min"


    def get_genre(self , movie : Movie):

        if cache.get(f"movie_data_{movie.tmdb_id}"):
            data = cache.get(f"movie_data_{movie.tmdb_id}")

            print("***************cache hit ******************")
            print(cache.ttl("movie_data_{movie.tmdb_id}"))

            if(cache.ttl(f"movie_data_{movie.tmdb_id}") < 20):
                cache.set(f"movie_data_{movie.tmdb_id}",data, timeout=3600)

        else:
            data = get_movie_information(movie.tmdb_id)
            cache.set(f"movie_data_{movie.tmdb_id}",data)

        search_genre = "genres[*].name"
        genre = jmespath.search(search_genre,data)
        return genre
        
    def get_title(self , movie : Movie):

        if cache.get(f"movie_data_{movie.tmdb_id}"):
            data = cache.get(f"movie_data_{movie.tmdb_id}")
            print("***************cache hit ******************")
        else:
            data = get_movie_information(movie.tmdb_id)
            cache.set(f"movie_data_{movie.tmdb_id}",data)

        search_genre = "title"
        genre = jmespath.search(search_genre,data)
        return genre
        
    def get_poster(self, movie: Movie):

        if cache.get(f"movie_data_{movie.tmdb_id}"):
            data = cache.get(f"movie_data_{movie.tmdb_id}")
            print("***************cache hit ******************")
        else:
            data = get_movie_information(movie.tmdb_id)
            cache.set(f"movie_data_{movie.tmdb_id}",data)
        search_poster_path = "poster_path"
        poster = jmespath.search(search_poster_path,data)
        return f"https://image.tmdb.org/t/p/original{poster}"

    def get_overview(self, movie: Movie):
        data = dict()
        if cache.get(f"movie_data_{movie.tmdb_id}"):
            data = cache.get(f"movie_data_{movie.tmdb_id}")
            print("***************cache hit ******************")
        else:
            data = get_movie_information(movie.tmdb_id)
            cache.set(f"movie_data_{movie.tmdb_id}",data)

        search_overview = "overview"
        overview = jmespath.search(search_overview,data)
        return overview

    def get_tagline(self, movie: Movie):

        if cache.get(f"movie_data_{movie.tmdb_id}"):
            data = cache.get(f"movie_data_{movie.tmdb_id}")
            print("***************cache hit ******************")
        else:
            data = get_movie_information(movie.tmdb_id)
            cache.set(f"movie_data_{movie.tmdb_id}",data)

        search_tagline = "tagline"
        tagline = jmespath.search(search_tagline,data)
        return tagline

    def get_production_company(self, movie: Movie):
        
        if cache.get(f"movie_data_{movie.tmdb_id}"):
            data = cache.get(f"movie_data_{movie.tmdb_id}")
            print("***************cache hit ******************")
        else:
            data = get_movie_information(movie.tmdb_id)
            cache.set(f"movie_data_{movie.tmdb_id}",data)

        search_prod_comp = "production_companies[*].name"
        prod_comp = jmespath.search(search_prod_comp,data)
        return prod_comp

    
    def get_release_date(self, movie: Movie):

        if cache.get(f"movie_data_{movie.tmdb_id}"):
            data = cache.get(f"movie_data_{movie.tmdb_id}")
            print("***************cache hit ******************")
        else:
            data = get_movie_information(movie.tmdb_id)
            cache.set(f"movie_data_{movie.tmdb_id}",data)

        search_release_date = "release_date"
        release_date = jmespath.search(search_release_date,data)
        return release_date


    def get_spoken_language(self, movie: Movie):

        if cache.get(f"movie_data_{movie.tmdb_id}"):
            data = cache.get(f"movie_data_{movie.tmdb_id}")
            print("***************cache hit ******************")
        else:
            data = get_movie_information(movie.tmdb_id)
            cache.set(f"movie_data_{movie.tmdb_id}",data)

        search_spoken_lang = "spoken_languages[*].english_name"
        spoken_lang = jmespath.search(search_spoken_lang,data)
        return spoken_lang
    

