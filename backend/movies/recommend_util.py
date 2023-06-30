import os
import pandas as pd
import numpy as np
import pickle
from django.conf import settings
from . import utils



def load_movies_data_pkl():
    file_path = os.path.join(settings.PKL_URL,'movies.pkl')
    with open(file_path,'rb') as file:
        movies_data_pkl = pickle.load(file)
    
    return movies_data_pkl




def load_similarity_data_pkl():
    file_path = os.path.join(settings.PKL_URL,'similarity.pkl')
    with open(file_path,'rb') as a_file:
        similarity_data_pkl = pickle.load(a_file)
    
    return similarity_data_pkl



def recommend(movie_name):
    # loading movies dataset
    movies_data_pkl = load_movies_data_pkl()
    movies_data_pkl = pd.DataFrame(movies_data_pkl)

    # loading similarity data among all the dataset
    similarity_data_pkl = load_similarity_data_pkl()
    similarity_data_pkl = np.array(similarity_data_pkl)
    
    movie_name = movie_name.capitalize()

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

    return new_data
  