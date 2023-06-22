from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Storyteller, Historian

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class StorytellerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Storyteller
        fields = ['user', 'bio', 'credentials']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        storyteller = Storyteller.objects.create(user=user, **validated_data)
        return storyteller

class HistorianSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Historian
        fields = ['user', 'bio', 'credentials', 'verified']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        historian = Historian.objects.create(user=user, **validated_data)
        return historian
