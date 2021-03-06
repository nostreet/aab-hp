from django.contrib import admin
from .models import SignedUp

class SignedUpAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact_email', 'paid', 'event','signup_date', 'dietary', "single_day_pass",
            "weekend_pass", "single_day_pass_normal", "weekend_pass_normal"]
    search_fields = ('first_name', 'last_name', 'contact_email','event' )
admin.site.register(SignedUp, SignedUpAdmin)
# Register your models here.
fields= ["first_name", "last_name", "contact_email", "contact_phone", "single_day_pass",
        "weekend_pass", "single_day_pass_normal", "weekend_pass_normal",
        "beeclub_asso", "which_club", "event","dietary", ]
