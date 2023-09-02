
from django.core.cache import cache
import dotenv
import jmespath

import requests
import json
import os 

from dotenv import load_dotenv
load_dotenv()


url = ""
response = ""
API_KEY = os.getenv('API_KEY_TMDB')

def movie_information(tmdb_id): 
    print("\n\n***************************** API Called *********************************\n\n")
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"

    response = requests.get(url)
    data = json.loads(response.text)
    cache.set(f"movie_data_{tmdb_id}",data, timeout=3600)
    return data



def returnData(tmdb_id):
    movieData = dict()
    if cache.get(f"movie_data_{tmdb_id}"):
        print(f"+++++++++++++++++++++ cache hit +++++++++++++++++++++")
        movieData = cache.get(f"movie_data_{tmdb_id}")
    else:
        print(f"+++++++++++++++++++++ cache miss +++++++++++++++++++++")
        movieData = movie_information(tmdb_id)
        cache.set(f"movie_data_{tmdb_id}",movieData)

    return movieData


def search_key(tmdb_id, search_string):
    data = returnData(tmdb_id=tmdb_id)
    search_ = search_string
    required_data = jmespath.search(search_, data)
    return required_data

def imdb_id(tmdb_id):
    return search_key(tmdb_id,"imdb_id")

def original_language(tmdb_id):
    return search_key(tmdb_id,"original_language")

def original_title(tmdb_id):
    return search_key(tmdb_id,"original_title")

def runtime(tmdb_id):
    return search_key(tmdb_id,"runtime")

def title(tmdb_id):
    return search_key(tmdb_id,"title")

def genre(tmdb_id):
    return search_key(tmdb_id,"genres[*].name")
    




def poster(tmdb_id):

    data = returnData(tmdb_id)        # calling returnData() # from utils.py 
    search_poster_path = "poster_path"
    poster = jmespath.search(search_poster_path,data)
    if poster == None:
        return f"Poster Not Available"

    return f"https://image.tmdb.org/t/p/original{poster}"

def overview(tmdb_id):
    return search_key(tmdb_id,"overview")

def tagline(tmdb_id):
    return search_key(tmdb_id,"tagline")

def production_company(tmdb_id):
    return search_key(tmdb_id,"production_companies[*].name")

def release_date(tmdb_id):
    return search_key(tmdb_id,"release_date")

def spoken_language(tmdb_id):
    return search_key(tmdb_id,"spoken_languages[*].english_name")

def forMovieOutsideDB(tmdb_id):
    data = dict()
    data.update(
        {
            'tmdb_id' : tmdb_id,
            'imdb_id' : imdb_id(tmdb_id),
            'original_language' : original_language(tmdb_id),
            'original_title' : original_title(tmdb_id),
            'title' : title(tmdb_id),
            'runtime' : runtime(tmdb_id),
            'genre': genre(tmdb_id),
            'poster': poster(tmdb_id),
            'overview' : overview(tmdb_id),
            'tagline' :  tagline(tmdb_id),
            'prod_company' : production_company(tmdb_id),
            'release_date' : release_date(tmdb_id),
            'spoken_language' : spoken_language(tmdb_id)
        }
    )
    data = json.dumps(data)
    data = json.loads(data)
    return data



def parse_movie_list(jsonData):
    data = dict(jsonData)

    id_list = []
    results = data.get("results", [])
    
    
    for item in results:
        item_id = item.get("id")
        if item_id is not None:
            id_list.append(item_id)

    movies_data = []
    for each_id in id_list:
        movie = forMovieOutsideDB(each_id)
        movies_data.append(movie)

    new_data = dict({"movies" : movies_data})

    data = json.dumps(new_data)
    data = json.loads(data)

    return data




# parsing OrderedDict

def parseOrderedDict(serializerData):
    new = list()
    for each in serializerData:
        new.append(dict(each))

    return new



def parseMovies_and_TV_List(api_url):

    response = requests.get(api_url)
    json_data = response.json()

    new = list()
    for each in json_data["results"]:
        new.append(forMovieOutsideDB(each["id"]))
    # print(new)
    return new