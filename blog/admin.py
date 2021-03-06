from django.contrib import admin
from .models import Post, Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ['post']
admin.site.register(Post)
admin.site.register(Image, ImageAdmin)
