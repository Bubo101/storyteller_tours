from django.contrib import admin
from .models import Tour, Stop, SubStop

# Register your models here.


class TourAdmin(admin.ModelAdmin):
    pass

class StopAdmin(admin.ModelAdmin):
    pass

class SubStopAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tour, TourAdmin)

admin.site.register(Stop, StopAdmin)

admin.site.register(SubStop, SubStopAdmin)