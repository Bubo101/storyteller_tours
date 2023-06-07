from django.contrib import admin
from .models import TourImage, TourAudio, TourVideo, StopAudio, StopImage, StopVideo, UserImage

# Register your models here.


class UserImageAdmin(admin.ModelAdmin):
    pass

class TourImageAdmin(admin.ModelAdmin):
    pass

class StopImageAdmin(admin.ModelAdmin):
    pass

class TourAudioAdmin(admin.ModelAdmin):
    pass

class StopAudioAdmin(admin.ModelAdmin):
    pass

class TourVideoAdmin(admin.ModelAdmin):
    pass

class StopVideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserImage, UserImageAdmin)

admin.site.register(TourImage, TourImageAdmin)

admin.site.register(StopImage, StopImageAdmin)

admin.site.register(TourAudio, TourAudioAdmin)

admin.site.register(StopAudio, StopAudioAdmin)

admin.site.register(TourVideo, TourVideoAdmin)

admin.site.register(StopVideo, StopVideoAdmin)
