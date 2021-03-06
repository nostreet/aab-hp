from django.db import models
from django.utils import timezone

class Event(models.Model):

    title = models.CharField(max_length=100,blank=False, default='')
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    event_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True,editable=False)

    def __str__(self):
         return self.title
