from django.shortcuts import render, redirect, get_object_or_404

from movieapp.models import Movie
from .models import MovieFavourite

def add_to_favourites(request,id):
        movie = Movie.objects.get(id=id)
        MovieFavourite.objects.get_or_create(user=request.user, movie=movie)
        return redirect('/favouritesapp/myfavmovies/')

def my_favourite_movies(request):
    movies = MovieFavourite.objects.filter(user=request.user)
    return render(request, 'favourite.html', {'movies': movies})

def remove_favourites(request,id):
         mv=get_object_or_404(MovieFavourite, user=request.user, movie_id=id)
         mv.delete()
         return redirect('/favouritesapp/myfavmovies/')