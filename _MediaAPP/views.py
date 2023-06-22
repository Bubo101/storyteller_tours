# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    TourImage, TourAudio, TourVideo,
    StopImage, StopAudio, StopVideo,
    UserImage
)
from .serializers import (
    TourImageSerializer, TourAudioSerializer, TourVideoSerializer,
    StopImageSerializer, StopAudioSerializer, StopVideoSerializer,
    UserImageSerializer
)

# GET and POST operations
@api_view(['GET', 'POST'])
def tour_images(request):
    if request.method == 'GET':
        tour_images = TourImage.objects.all()
        serializer = TourImageSerializer(tour_images, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TourImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def tour_audios(request):
    if request.method == 'GET':
        tour_audios = TourAudio.objects.all()
        serializer = TourAudioSerializer(tour_audios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TourAudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def tour_videos(request):
    if request.method == 'GET':
        tour_videos = TourVideo.objects.all()
        serializer = TourVideoSerializer(tour_videos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TourVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def stop_images(request):
    if request.method == 'GET':
        stop_images = StopImage.objects.all()
        serializer = StopImageSerializer(stop_images, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StopImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def stop_audios(request):
    if request.method == 'GET':
        stop_audios = StopAudio.objects.all()
        serializer = StopAudioSerializer(stop_audios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StopAudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def stop_videos(request):
    if request.method == 'GET':
        stop_videos = StopVideo.objects.all()
        serializer = StopVideoSerializer(stop_videos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StopVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_images(request):
    if request.method == 'GET':
        user_images = UserImage.objects.all()
        serializer = UserImageSerializer(user_images, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT and DELETE operations
@api_view(['PUT', 'DELETE'])
def tour_image_detail(request, pk):
    try:
        tour_image = TourImage.objects.get(pk=pk)
    except TourImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TourImageSerializer(tour_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tour_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def tour_audio_detail(request, pk):
    try:
        tour_audio = TourAudio.objects.get(pk=pk)
    except TourAudio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TourAudioSerializer(tour_audio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tour_audio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def tour_video_detail(request, pk):
    try:
        tour_video = TourVideo.objects.get(pk=pk)
    except TourVideo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TourVideoSerializer(tour_video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tour_video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def stop_image_detail(request, pk):
    try:
        stop_image = StopImage.objects.get(pk=pk)
    except StopImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StopImageSerializer(stop_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        stop_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def stop_audio_detail(request, pk):
    try:
        stop_audio = StopAudio.objects.get(pk=pk)
    except StopAudio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StopAudioSerializer(stop_audio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        stop_audio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# PUT and DELETE operations (continued)
@api_view(['PUT', 'DELETE'])
def stop_video_detail(request, pk):
    try:
        stop_video = StopVideo.objects.get(pk=pk)
    except StopVideo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StopVideoSerializer(stop_video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        stop_video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def user_image_detail(request, pk):
    try:
        user_image = UserImage.objects.get(pk=pk)
    except UserImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserImageSerializer(user_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


