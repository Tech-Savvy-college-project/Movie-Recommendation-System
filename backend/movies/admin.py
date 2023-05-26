from django.contrib import admin
from . import models
from django.core.cache import cache
# Register your models here.



@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['tmdb_id', 'imdb_id', 'original_title','original_language', 'runtime_']
    # 'poster', 'genre', 'release_date']
    list_per_page = 20
    search_fields = ['original_title', 'tmdb_id', 'imdb_id']

    @admin.display(ordering='runtime')
    def runtime_(self,movie):
        return f"{movie.runtime} min"
    
