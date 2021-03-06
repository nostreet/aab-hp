from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField

class Post(models.Model):
    #kind of a super User connection. only one person here
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True,editable=False)

    def __str__(self):
        return self.title

#multiupload
class Image(models.Model):
    post = models.ForeignKey('Post', related_name='images', blank=True, null=True)
    file = ThumbnailerImageField(upload_to='news-images', blank=True,
                                        resize_source=dict(size=(600, 600)))
    file2 = ThumbnailerImageField(upload_to='news-images',blank=True,
                                        resize_source=dict(size=(600, 600)))
    file3 = ThumbnailerImageField(upload_to='news-images',blank=True,
                                        resize_source=dict(size=(600, 600)))
    file4 = ThumbnailerImageField(upload_to='news-images',blank=True,
                                        resize_source=dict(size=(600, 600)))
    file5 = ThumbnailerImageField(upload_to='news-images',blank=True,
                                        resize_source=dict(size=(600, 600)))
    file6 = ThumbnailerImageField(upload_to='news-images',blank=True,
                                            resize_source=dict(size=(600, 600)))


    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]
