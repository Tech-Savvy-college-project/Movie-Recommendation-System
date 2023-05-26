from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import Movie
from .serializers import MoviesSerializer 

import requests
import json


# for caching

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)




# Create your views here.

# /movies
@api_view()
def movies_data(request):
    queryset = Movie.objects.all()[:100]
    serializer = MoviesSerializer(queryset, many=True)
    return Response(serializer.data)


# /movies/<tmdb-id>
@api_view()
def movie_detail(request,id):
    movie = get_object_or_404(Movie,tmdb_id=id)
    serializer = MoviesSerializer(movie)
    
    return Response(serializer.data)