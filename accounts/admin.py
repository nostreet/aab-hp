from django.contrib import admin
from accounts.models import UserProfileInfo
from django.utils.html import format_html
from django.contrib.auth.models import Permission
admin.site.register(Permission)

class AccountsAdmin(admin.ModelAdmin):

    def name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    # def image_tag(self, obj):
    #     return format_html('<img src="{}" width="100" height="100" />'.format(obj.profile_picture.url))

    # image_tag.short_description = 'Image'

    # list_display = ['name', 'city', 'mobile', 'image_tag', 'joined_date']
    list_display = ['name', 'city', 'mobile', 'joined_date']
# Register your models here.
admin.site.register(UserProfileInfo, AccountsAdmin)
