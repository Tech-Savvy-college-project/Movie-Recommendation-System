from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializers import MoviesSerializerInDB 

import requests
from .utils import forMovieOutsideDB, parse_movie_list




# for caching

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_KEY_TMDB')


# Create your views here.

# /movies
@api_view()
def movies_data(request):

    queryset = Movie.objects.all()[:100]
    serializer = MoviesSerializerInDB(queryset, many=True)
    return Response(serializer.data)


# /movies/<tmdb-id>
@api_view()
def movie_detail(request,id):
    try: 
        movie = Movie.objects.get(tmdb_id=id)
        serializer = MoviesSerializerInDB(movie)
    except Movie.DoesNotExist:
        return Response(forMovieOutsideDB(id))
    
    return Response(serializer.data)


