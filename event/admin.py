from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'event_date', 'published_date']

admin.site.register(Event, EventAdmin)
# Register your models here.
