from django.shortcuts import render

from django.http import HttpResponse
from .models import Movies, Director,Genres


def index(request):

    All_Movies = Movies.objects.all()
    #lk = Movies.objects.all()
    #kk = Director.objects.all()
    html =''
    for movies in All_Movies:
        url = '/movies/' + str(movies.id) + '/'
        html += '<a href ="'+ url +'">' + movies.movie_name + '<a/><br>'
    return HttpResponse(html)


def detail(request, movie_id):
    return HttpResponse("<h1>this is the details of the " + str(movie_id) + " movies<h1>")