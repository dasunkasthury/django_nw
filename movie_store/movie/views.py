

#from django.http import HttpResponse
from builtins import KeyError

from .models import Movies,Director,Genres
#from django.template import loader
from django.shortcuts import render ,get_object_or_404
from django.http import Http404

def index(request):

    All_Movies = Movies.objects.all()

    return render(request,'movie/index.html',{'All_Movies':All_Movies})




def detail(request, movie_id):

    movie = get_object_or_404(Movies,pk=movie_id)

    return render(request, 'movie/detail.html', {'movie': movie})




def favourite(request, movie_id):

    movie = get_object_or_404(Movies,pk=movie_id)
    try:
        selected_song = movie.genres.get(pk =request.POST['genres'])
    except(KeyError, Genres.DoesNotExist):
        return render(request, 'movie/detail.html', {
            'movie': movie,
            'error_message': "you did not select a right genres"


        })
    else:
        selected_song.is_favourite= True
        selected_song.save()
        return render(request, 'movie/detail.html', {'movie': movie})



