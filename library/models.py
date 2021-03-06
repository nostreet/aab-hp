from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    storyline = models.TextField()
    book_cover = ThumbnailerImageField(upload_to='book_cover',blank=True,
                                        resize_source=dict(size=(350, 350)))
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
         return self.title
