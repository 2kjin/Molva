import json
import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer, GenreSerializer, ActorSerializer, DirectorSerializer

from .models import Movie, Genre, Actor, Director
from django.http import HttpResponse
# Create your views here.

def create_json(request):
    lst_movie = []
    # movie.json 생성
    for i in range(1,6):
        url_movie = f'https://api.themoviedb.org/3/movie/popular?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=ko-kr&page={i}'
        dict_movie = requests.get(url_movie).json()
        lst_movie += dict_movie.get('results')

    # genre.json 생성 
    url_genre = 'https://api.themoviedb.org/3/genre/movie/list?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=ko-kr'
    dict_genre = requests.get(url_genre).json()
    lst_genre = dict_genre.get('genres')
    for i in lst_genre:
        genre = Genre()
        genre.id = i.get('id')
        genre.name = i.get('name')
        genre.save()

    for j in lst_movie:
        tmdb_id = j.get('id')
        if not j.get('overview') or not j.get('poster_path') or not j.get('backdrop_path'):
            continue
        movie = Movie()
        movie.id = j.get('id')
        movie.title = j.get('title')
        movie.overview = j.get('overview')
        movie.popularity = j.get('popularity')
        movie.poster_path = j.get('poster_path')
        movie.release_date = j.get('release_date')
        movie.vote_average = j.get('vote_average')
        # pprint(movie.keys)
        movie.save()

        # 장르 연동
        for k in j.get('genre_ids'):
            # pprint(k)
            movie.genres.add(k)
        
        # 직업
        url_credits = f'https://api.themoviedb.org/3/movie/{tmdb_id}/credits?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=ko-kr'
        response = requests.get(url_credits)
        movie_credits = response.json()

        # 배우
        casts = movie_credits['cast']

        for cast in casts[:7]:
            if not cast.get('id') or not cast.get('name'):
                continue
            actor = Actor()
            actor.id = cast.get('id')
            actor.name = cast.get('name')
            actor.save()
            movie.actors.add(cast.get('id'))

        #감독
        directors = []
        crews = movie_credits['crew']
        for crew in crews:
            if crew['job'] == "Director":
                directors.append(crew)
        
        for d in directors:
            if not d.get('id') or not d.get('name'):
                continue
            director = Director()
            director.id = d.get('id')
            director.name = d.get('name')
            director.save()
            movie.directors.add(d.get('id'))

    # print('성공!')
    return HttpResponse()

@api_view(['GET'])
def movie(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def genre(request):
    genres = Genre.objects.all()
    serializers = GenreSerializer(genres, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def actor(request):
    actors = Actor.objects.all()
    serializers = ActorSerializer(actors, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def director(request):
    directors = Director.objects.all()
    serializers = DirectorSerializer(directors, many=True)
    return Response(serializers.data)
