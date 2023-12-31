from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# from movies.models import Movie
from movies.serializers import ReviewSerializer, MovieTitleSerializer
from .serializers import ProfileSeriallizer
from community.serializers import PostListSerializer


@api_view(['DELETE'])
def user_delete(request):
    request.delete()     # 탈퇴 후 로그아웃
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    if request.method == 'GET':
        # reviews = person.review_set.all()
        # favorites = person.like_movies.all()
        # posts = person.like_reviews.all()
        # watchlist = person.watch_list.all()
        # watched = person.watched_movies.all()

        # if person.follower.filter(pk=request.user.pk).exists():
        #     is_followed = True
        # else:
        #     is_followed = False

        context = {
            'user_id': person.id,
            'username': person.username,
            # 'reviews': ReviewSerializer(reviews, many=True).data,
            # 'favorites': MovieTitleSerializer(favorites, many=True).data,
            # 'is_followed': is_followed,
            # 'following_count': person.following.count(),
            # 'follower_count': person.follower.count(),
            # 'watch_list': MovieTitleSerializer(watchlist, many=True).data,
            # 'watched_movies': MovieTitleSerializer(watched, many=True).data,
            # 'posts': PostListSerializer(posts, many=True).data,
        }
        return Response(context)
    

    elif request.method == 'PUT':
        if person == request.user:
            serializer = ProfileSeriallizer(person, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)

    if person != request.user:
        if person.follower.filter(pk=request.user.pk).exists():
            person.follower.remove(request.user)
            is_followed = False

        else:
            person.follower.add(request.user)
            is_followed = True
        
        context = {
            'is_followed': is_followed,
            'follow_count': person.follower.count(),
            'following_count': person.following.count()
        }
        
        return JsonResponse(context)
