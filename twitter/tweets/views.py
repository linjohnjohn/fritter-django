from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from .serializers import FreetSerializer, TweetActionSerializer, TweetCreateSerializer
# from .models import Freet
# # Create your views here.

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def freet_create_view(request, *args, **kwargs):
#     serializer = FreetCreateSerializer(data=request.POST)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user)
#         return Response(serializer.data, status=201)

# @api_view(['GET'])
# def freet_detail_view(request, id, *args, **kwargs):
#     qs = Freet.objects.filter(id=id)
#     if not qs.exists():
#         return Response({}, status=404)
#     freet = qs.first()
#     serializer = FreetSerializer(freet)
#     return Response(serializer.data, status=200)


# @api_view(['POST'])
# def freet_action_view(request, *arg, **kwargs):
#     serializer = FreetActionSerializer(data=request.POST)
#     if serializer.is_valid(raise_exception=True):
#         data = serializer.validated_data
#         freet_id = data.get('id')
#         action = data.get('action')
#         content = data.get('content')
#         qs = Freet.objects.filter(id=tweet_id)
    
#         if not qs.exist():
#             return Response({}, status=404)
#         obj = qs.first()

#         if action == 'like':
#             obj.likes.add(request.user)
#             serializer = FreetSerializer(obj)
#             return Response(serializer.data, status=200)
#         elif action == 'unlike':
#             obj.likes.remove(request.user)
#             serializer = FreetSerializer(obj)
#             return Response(serializer.data, status=200)
#         elif action == 'refreet':
#             new_freet = Freet.objects.create(user=request.user, parent=obj, content=content)
#             serializer = FreetSerializer(new_tweet)
#             return Response(serializer.data, status=201)

# @api_view(['GET'])
# def freet_list_view(request, *args, **kwargs):
#     qs = Freet.objects.all()
#     serializer = FreetSerializer(qs, many=True)
#     return Response(serializer.data)