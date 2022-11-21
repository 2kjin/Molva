import json
import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ReviewSerializer, MovieListSerializer, MovieDetailSerializer

from .models import Movie, Genre, Actor, Director, Review, Watch_Provider
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from pprint import pprint

def create_json(request):
    lst_movie = []
    # movie.json 생성
    for i in range(1,50):
        url_movies = f'https://api.themoviedb.org/3/movie/popular?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=ko-kr&page={i}'
        dict_movies = requests.get(url_movies).json()
        lst_movie += dict_movies.get('results')

    # genre.json 생성 
    url_genre = 'https://api.themoviedb.org/3/genre/movie/list?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=ko-kr'
    dict_genre = requests.get(url_genre).json()
    lst_genre = dict_genre.get('genres')
    for i in lst_genre:
        genre = Genre()
        genre.genre_id = i.get('id')
        genre.name = i.get('name')
        genre.save()

    for j in lst_movie:
        tmdb_id = j.get('id')
        # movie_detail 정보
        url_movie = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=ko-kr'
        dict_movie = requests.get(url_movie).json()

        # ott 관련 정보
        url_ott = f'https://api.themoviedb.org/3/movie/{tmdb_id}/watch/providers?api_key=b0aa983e176b4c8d5f9a1c93be84107b'
        dict_ott = requests.get(url_ott).json()
        lst_ott = dict_ott.get('results').get('KR')
        
        if not j.get('overview') or not j.get('poster_path') or not j.get('backdrop_path') or not j.get('backdrop_path'):
            continue

        movie = Movie()
        # ott 관련 정보가 있는 경우에만 받기
        set1 = set()
        if lst_ott:
            if lst_ott.get('buy'):
                for p in lst_ott.get('buy'):
                    set1.add((p.get('provider_id'),p.get('logo_path')))
            if lst_ott.get('rent'):
                for p in lst_ott.get('rent'):
                    set1.add((p.get('provider_id'),p.get('logo_path')))
            if lst_ott.get('flatrate"'):
                for p in lst_ott.get('flatrate"'):
                    set1.add((p.get('provider_id'),p.get('logo_path')))
        lst = list(set1)
        
        movie.movie_id = j.get('id')
        movie.title = j.get('title')
        movie.overview = j.get('overview')
        movie.runtime = dict_movie.get('runtime')
        movie.popularity = j.get('popularity')
        movie.vote_count = j.get('vote_count')
        movie.poster_path = j.get('poster_path')
        movie.release_date = j.get('release_date')
        movie.vote_average = j.get('vote_average')
        movie.backdrop_path = j.get('backdrop_path')
        movie.save()

        # ott_path 연동
        for o in lst:
            ott = Watch_Provider()
            ott.ott_id = o[0]
            ott.ott_path = o[1]
            ott.save()
            movie.ott_paths.add(o[0])

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
            if not cast.get('id') or not cast.get('name') or not cast.get('profile_path'):
                continue
            actor = Actor()
            actor.actor_id = cast.get('id')
            actor.name = cast.get('name')
            actor.profile_path = cast.get('profile_path')
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
            director.director_id = d.get('id')
            director.name = d.get('name')
            director.save()
            movie.directors.add(d.get('id'))

    # print('성공!')
    return HttpResponse()


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    # movie = get_object_or_404(Movie.objects.prefetch_related('actors','genres','directors', 'ott_paths'), pk=movie_id)

    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieDetailSerializer(movie)

    return Response(serializer.data)


def like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if movie.like_users.filter(pk=movie_id).exists():
        movie.like_users.remove(request.user)
        is_liked = False
    
    else:
        movie.like_users.add(request.user)
        is_liked = True
    
    context = {
        'is_liked': is_liked,
        'like_count' : movie.like_users.count()
    }
    return JsonResponse(context)


@api_view(['POST'])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 댓글 삭제
    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 댓글 수정
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)