from django.contrib import admin
from .models import Movie, Event, GroupEventManager

# Register your models here.
admin.site.register(Movie)


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Vote", {"fields": ["event_start_vote_time", "event_end_vote_time"]}),
        ("Event", {"fields": ["event_name", "event_location", "event_time"]}),
    ]


admin.site.register(Event, EventAdmin)

admin.site.register(GroupEventManager)
