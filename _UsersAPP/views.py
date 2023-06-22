from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Storyteller, Historian
from .serializers import (
    StorytellerSerializer, HistorianSerializer, UserSerializer
)

# GET and POST operations
@api_view(['GET', 'POST'])
def storyteller_list(request):
    if request.method == 'GET':
        storytellers = Storyteller.objects.all()
        serializer = StorytellerSerializer(storytellers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        storyteller_serializer = StorytellerSerializer(data=request.data)

        if user_serializer.is_valid(raise_exception=True) and storyteller_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
            storyteller = storyteller_serializer.save(user=user)
            response_serializer = StorytellerSerializer(storyteller)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response({
            'user_errors': user_serializer.errors,
            'storyteller_errors': storyteller_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def historian_list(request):
    if request.method == 'GET':
        historians = Historian.objects.all()
        serializer = HistorianSerializer(historians, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        historian_serializer = HistorianSerializer(data=request.data)

        if user_serializer.is_valid(raise_exception=True) and historian_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
            historian = historian_serializer.save(user=user)
            response_serializer = HistorianSerializer(historian)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response({
            'user_errors': user_serializer.errors,
            'historian_errors': historian_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

# PUT and DELETE operations
@api_view(['PUT', 'DELETE'])
def storyteller_detail(request, pk):
    try:
        storyteller = Storyteller.objects.get(pk=pk)
    except Storyteller.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        user_serializer = UserSerializer(storyteller.user, data=request.data)
        storyteller_serializer = StorytellerSerializer(storyteller, data=request.data)

        if user_serializer.is_valid(raise_exception=True) and storyteller_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
            storyteller = storyteller_serializer.save(user=user)
            response_serializer = StorytellerSerializer(storyteller)
            return Response(response_serializer.data)
        return Response({
            'user_errors': user_serializer.errors,
            'storyteller_errors': storyteller_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        storyteller.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def historian_detail(request, pk):
    try:
        historian = Historian.objects.get(pk=pk)
    except Historian.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        user_serializer = UserSerializer(historian.user, data=request.data)
        historian_serializer = HistorianSerializer(historian, data=request.data)

        if user_serializer.is_valid(raise_exception=True) and historian_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
            historian = historian_serializer.save(user=user)
            response_serializer = HistorianSerializer(historian)
            return Response(response_serializer.data)
        return Response({
            'user_errors': user_serializer.errors,
            'historian_errors': historian_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        historian.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
