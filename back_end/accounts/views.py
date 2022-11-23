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

# Create your views here.

# @api_view(['DELETE'])
# def user_delete(request):
#     request.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    reviews = person.review_set.all()
    favorites = person.like_movies.all()
    context = {
        'user_id': person.id,
        'username': person.username,
        'reviews': ReviewSerializer(reviews, many=True).data,
        'favorites': MovieTitleSerializer(favorites, many=True).data,
    }
    return Response(context)
