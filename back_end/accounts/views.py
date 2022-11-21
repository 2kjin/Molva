# from django.shortcuts import render
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404, get_list_or_404
# from django.contrib.auth import get_user_model

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

# from .serializers import ProfileSeriallizer

# Create your views here.

# @api_view(['DELETE'])
# def user_delete(request):
#     request.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def profile(request, user_pk):
#     User = get_user_model()
#     user = User.objects.get(pk=user_pk)

#     if user == request.user:
#         if request.method == 'PUT':
#             serializer = ProfileSeriallizer(user, data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data)
#     return Response(status=status.HTTP_403_FORBIDDEN)