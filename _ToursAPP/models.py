from django.db import models
from _UsersAPP.models import Storyteller, Historian

class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    price = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    hour_duration = models.SmallIntegerField()
    minute_duration = models.SmallIntegerField()
    rating = models.FloatField(null=True, blank=True)
    storyteller = models.ForeignKey(Storyteller, on_delete=models.PROTECT, related_name='tour')
    historian = models.ManyToManyField(Historian, related_name='tour', blank=True)

class Stop(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='stops')
    location = models.CharField(max_length=255)
    description = models.TextField(default='')
    order = models.SmallIntegerField()
    type = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

class SubStop(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='sub_stop')
    order = models.SmallIntegerField()



# class Purchase(models.Model):
#     user = models.ForeignKey('users.User', on_delete=models.CASCADE)
#     tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
#     purchase_date = models.DateTimeField(auto_now_add=True)
    # Other fields related to purchase information



