
from django.core.cache import cache
import dotenv

import requests
import json
import os 

from dotenv import load_dotenv
load_dotenv()


url = ""
response = ""
API_KEY = os.getenv('API_KEY_TMDB')

def get_movie_information(tmdb_id): 
    print("\n\n***************************** API Called *********************************\n\n")
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"

    response = requests.get(url)
    data = json.loads(response.text)
    cache.set("movie_data_{movie.tmdb_id}",data, timeout=3600)
    return data
