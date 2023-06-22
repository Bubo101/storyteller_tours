# serializers.py

from rest_framework import serializers
from .models import (
    TourImage, TourAudio, TourVideo,
    StopImage, StopAudio, StopVideo,
    UserImage
)

class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = '__all__'

class TourAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourAudio
        fields = '__all__'

class TourVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourVideo
        fields = '__all__'

class StopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopImage
        fields = '__all__'

class StopAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopAudio
        fields = '__all__'

class StopVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopVideo
        fields = '__all__'

class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = '__all__'
