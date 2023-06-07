from django.contrib import admin
from .models import User, Storyteller, Historian


class StorytellerAdmin(admin.ModelAdmin):
    pass

class HistorianAdmin(admin.ModelAdmin):
    pass



admin.site.register(Storyteller, StorytellerAdmin)

admin.site.register(Historian, HistorianAdmin)