# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

# from django.shortcuts import get_list_or_404, get_object_or_404
# from django.contrib.auth import get_user_model
# from .serializers import 
# from .models import Post, Comment
# from operator import itemgetter

# from django.db.models import Q



# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def community_list(request):
#     if request.method == 'GET':
#         # Communities = Community.objects.all()
#         Communities = get_list_or_404(Community)
#         serializer = CommunityListSerializer(Communities, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CommunitySerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # serializer.save()
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'DELETE', 'PUT'])
# def community_detail(request, community_pk):
#     # community = Community.objects.get(pk=community_pk)
#     community = get_object_or_404(Community, pk=community_pk)

#     if request.method == 'GET':
#         serializer = CommunitySerializer(community)
#         print(serializer.data)
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         community.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = CommunitySerializer(community, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET'])
# def comment_list(request):
#     if request.method == 'GET':
#         # comments = Comment.objects.all()
#         comments = get_list_or_404(Comment)
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)


# @api_view(['GET', 'DELETE', 'PUT'])
# def comment_detail(request, comment_pk):
#     # comment = Comment.objects.get(pk=comment_pk)
#     comment = get_object_or_404(Comment, pk=comment_pk)

#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

    


# @api_view(['POST'])
# def comment_create(request, community_pk):
#     # community = Community.objects.get(pk=community_pk)
#     community = get_object_or_404(Community, pk=community_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(community=community)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
