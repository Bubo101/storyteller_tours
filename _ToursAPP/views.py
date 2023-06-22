from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tour, Stop, SubStop
from .serializers import (
    TourSerializer, StopSerializer, SubStopSerializer
)

# GET and POST operations
@api_view(['GET', 'POST'])
def tour_list(request):
    if request.method == 'GET':
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def stop_list(request):
    if request.method == 'GET':
        stops = Stop.objects.all()
        serializer = StopSerializer(stops, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def substop_list(request):
    if request.method == 'GET':
        substops = SubStop.objects.all()
        serializer = SubStopSerializer(substops, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubStopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT and DELETE operations
@api_view(['PUT', 'DELETE'])
def tour_detail(request, pk):
    try:
        tour = Tour.objects.get(pk=pk)
    except Tour.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TourSerializer(tour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def stop_detail(request, pk):
    try:
        stop = Stop.objects.get(pk=pk)
    except Stop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StopSerializer(stop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        stop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def substop_detail(request, pk):
    try:
        substop = SubStop.objects.get(pk=pk)
    except SubStop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SubStopSerializer(substop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        substop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
