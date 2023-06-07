from django.db import models
from _ToursAPP.models import Tour, Stop, SubStop
from django.contrib.auth.models import User


class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='images/tour_images')
    caption = models.CharField(max_length=255, default='')
    is_main_image = models.BooleanField(default=False)

class TourAudio(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='audio')
    audio = models.FileField(upload_to='audio/tour_audio')
    script = models.TextField(default='')
    is_main_audio = models.BooleanField(default=False)

class TourVideo(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='video')
    video = models.FileField(upload_to='video/tour_video')
    description = models.TextField(default='')
    script = models.TextField(default='')
    is_main_video = models.BooleanField(default=False)

class StopImage(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='image')
    sub_stop = models.ForeignKey(SubStop, on_delete=models.PROTECT, related_name='image', null=True, blank=True)
    image = models.ImageField(upload_to='images/stop_images')
    caption = models.CharField(max_length=255, default='')
    is_stop_main = models.BooleanField(default=False)
    is_sub_main = models.BooleanField(default=False)

class StopAudio(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='audio')
    sub_stop = models.ForeignKey(SubStop, on_delete=models.PROTECT, related_name='audio', null=True, blank=True)
    audio = models.FileField(upload_to='audio/stop_audio')
    script = models.TextField(default='')
    is_stop_main = models.BooleanField(default=False)
    is_sub_main = models.BooleanField(default=False)

class StopVideo(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='video')
    sub_stop = models.ForeignKey(SubStop, on_delete=models.PROTECT, related_name='video', null=True, blank=True)
    video = models.FileField(upload_to='video/stop_video')
    description = models.TextField(default='')
    script = models.TextField(default='')
    is_stop_main = models.BooleanField(default=False)
    is_sub_main = models.BooleanField(default=False)

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='images/user_images')
    is_main_image = models.BooleanField(default=False)