from django.contrib import admin
from .models import Book
from django.utils.html import format_html
# Register your models here.

class LibraryAdmin(admin.ModelAdmin):

    def book_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.book_cover.url))

    book_tag.short_description = 'Image'

    list_display = ['book_tag','title', 'author', 'created_date']

    search_fields = ['title', 'author']

admin.site.register(Book, LibraryAdmin)
