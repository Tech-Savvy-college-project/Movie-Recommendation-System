from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializers import MoviesSerializerInDB 

import requests
from .utils import forMovieOutsideDB, parse_movie_list, parseOrderedDict, parseMovies_and_TV_List
from . import recommend_util


from asgiref.sync import sync_to_async






# for caching


from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_KEY_TMDB')


# Create your views here.

# /movies/ 
@sync_to_async
@api_view()
def index(request):

    queryset = Movie.objects.all()[:10]
    serializer = MoviesSerializerInDB(queryset, many=True)
    movies = parseOrderedDict(serializerData=serializer.data) 
    # print(serializer.data)
    # print("=============================================================================================")
    # print(new)
    # return render(request, "web/index.html",{"movies":movies})
    return Response(serializer.data)


# /movies/<tmdb-id>/
@api_view()
def detail(request,movie_id):
    try: 
        movie = Movie.objects.get(tmdb_id=movie_id)
        serializer = MoviesSerializerInDB(movie)
    except Movie.DoesNotExist:
        print("outside db")
        movie_detail = forMovieOutsideDB(movie_id);
        # return render(request, "web/detail.html",{"movies" : movie_detail})
        return Response(forMovieOutsideDB(movie_id))
    print("inside db")
    print(serializer.data)
    
    # return render(request, "web/detail.html",{"movies":serializer.data})
    return Response(serializer.data)





@sync_to_async
# /movies/search/?q={your_query}
@api_view(['GET'])
def search(request):
    query = request.GET.get('q')

    api_url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=true&language=en-US&page=1&api_key={API_KEY}"
    # Send a GET request to the TMDB API
    response = requests.get(api_url)
    json_data = response.json()

    return Response(parse_movie_list(json_data))




# /movies/popular/
@api_view(['GET'])
def popular(request):

    # Send a GET request to the TMDB API
    api_url1 = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page=1&api_key={API_KEY}"
    movie_list1 = parseMovies_and_TV_List(api_url=api_url1)
    api_url2 = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page=2&api_key={API_KEY}"
    movie_list2 = parseMovies_and_TV_List(api_url=api_url2)
    api_url3 = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page=3&api_key={API_KEY}"
    movie_list3 = parseMovies_and_TV_List(api_url=api_url3)

    movies = [item for sublist in [movie_list1, movie_list2, movie_list3] for item in sublist] 
    
    return Response({"popular_movies": movie_list1})
    return Response(parseMovies_and_TV_List(movies))



# /movies/upcoming/
@api_view(['GET'])
def upcoming(request):

    # Send a GET request to the TMDB API
    api_url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}"
    movie_list = parseMovies_and_TV_List(api_url=api_url)
    # api_url2 = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page=2&api_key={API_KEY}"
    # movie_list2 = parsePopularMovies(api_url=api_url2)
    # api_url3 = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page=3&api_key={API_KEY}"
    # movie_list3 = parsePopularMovies(api_url=api_url3)

    # movies = [item for sublist in [movie_list1, movie_list2, movie_list3] for item in sublist] 
    
    return Response(movie_list)



# /genres/
@api_view(['GET'])
def genre(request):
    
    api_url = f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={API_KEY}"
    response = requests.get(api_url)
    json_data = response.json()

    return Response(json_data)




# /genres/movies/?with_genres={genre_id}
@api_view(['GET'])
def genreMovies(request):
    genreID = request.GET.get('with_genres')
    api_url = f"https://api.themoviedb.org/3/discover/movie?with_genres={genreID}&api_key={API_KEY}"
    response = requests.get(api_url)
    json_data = response.json()
 
    return Response(parse_movie_list(json_data))


# http://127.0.0.1:8000/trailer/114461/
# movie trailer
@api_view(['GET'])
def movie_trailer(request,movie_id):
    api_url = f"https://api.themoviedb.org/3/tv/{movie_id}/videos?language=en-US?&api_key={API_KEY}&append_to_response=videos"
    response = requests.get(api_url)
    json_data = response.json()
 
    return Response(json_data)



# /movies/recommend/?movie_name={name of movie}
@api_view(['GET'])
def recommend(request):
    movie_name = request.GET.get('movie_name')
    json_data = recommend_util.recommend(movie_name)



    return Response(json_data)

