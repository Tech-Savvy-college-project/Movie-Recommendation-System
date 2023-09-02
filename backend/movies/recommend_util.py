import os
import pandas as pd
import numpy as np
import pickle
from django.conf import settings
from . import utils
from django.core.cache import cache


def load_movies_data_pkl():

    file_path = os.path.join(settings.PKL_URL,'movies.pkl')

    if cache.get(f"movies_pkl") is not None:
        movies_data_pkl = cache.get(f"movies_pkl") 
    else:
        with open(file_path,'rb') as file:
            movies_data_pkl = pickle.load(file)
            cache.set("movies_pkl",movies_data_pkl,timeout=3600)
        
    return movies_data_pkl




def load_similarity_data_pkl():

    file_path = os.path.join(settings.PKL_URL,'similarity.pkl')

    if cache.get(f"similarity_pkl") is not None:
        similarity_data_pkl = cache.get(f"similarity_pkl") 
    else:
        with open(file_path,'rb') as file:
            similarity_data_pkl = pickle.load(file)
            cache.set("similarity_pkl",similarity_data_pkl,timeout=3600)
    
    return similarity_data_pkl



def recommend(movie_name):
    # loading movies dataset
    new_data = dict({"movies" : []})
    movies_data_pkl = load_movies_data_pkl()
    movies_data_pkl = pd.DataFrame(movies_data_pkl)

    # loading similarity data among all the dataset
    similarity_data_pkl = load_similarity_data_pkl()
    similarity_data_pkl = np.array(similarity_data_pkl)
    
    movie_name = movie_name.capitalize()

    try:
        movie_index = movies_data_pkl[movies_data_pkl['title']==movie_name].index[0]
        distances = similarity_data_pkl[movie_index]
        movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
        

        #to fetch movies from indeces
        recommended_list = []
        for i in movies_list:
            movie = movies_data_pkl.iloc[i[0]].id
            # movie = utils.title(int(movies_data_pkl.iloc[i[0]].id))
            movie = utils.forMovieOutsideDB(int(movies_data_pkl.iloc[i[0]].id))
            recommended_list.append(movie)

        new_data = dict({"movies" : recommended_list})
    except IndexError:
        return new_data 
    return new_data
  