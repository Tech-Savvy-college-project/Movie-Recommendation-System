from rest_framework import serializers
from .models import Movie
from . import utils



class MoviesSerializerInDB(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['tmdb_id', 'imdb_id', 'original_language', 'original_title', 'title', 'runtime', 'genre', 'poster', 'overview', 'tagline', 'prod_company', 'release_date', 'spoken_language']
  

    
    title = serializers.SerializerMethodField(method_name='get_title')
    genre = serializers.SerializerMethodField(method_name='get_genre')    
    poster = serializers.SerializerMethodField(method_name='get_poster')
    overview = serializers.SerializerMethodField(method_name='get_overview')
    tagline = serializers.SerializerMethodField(method_name='get_tagline')
    prod_company = serializers.SerializerMethodField(method_name='get_production_company')
    release_date = serializers.SerializerMethodField(method_name='get_release_date')
    spoken_language = serializers.SerializerMethodField(method_name='get_spoken_language')
    # data = get_movie_information(Movie.tmdb_id)


    def get_title(self, movie : Movie):
        return utils.title(tmdb_id=movie.tmdb_id)

    def get_genre(self, movie : Movie):
        return utils.genre(tmdb_id=movie.tmdb_id)
        
    def get_poster(self, movie: Movie):
        return utils.poster(tmdb_id=movie.tmdb_id)

    def get_overview(self, movie: Movie):
        return utils.overview(tmdb_id=movie.tmdb_id)

    def get_tagline(self, movie: Movie):
        return utils.tagline(movie.tmdb_id)

    def get_production_company(self, movie: Movie):
       return utils.production_company(tmdb_id=movie.tmdb_id)

    
    def get_release_date(self, movie: Movie):
        return utils.release_date(tmdb_id=movie.tmdb_id)


    def get_spoken_language(self, movie: Movie):
        return utils.spoken_language(tmdb_id=movie.tmdb_id)
    
