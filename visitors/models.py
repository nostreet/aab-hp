from django.db import models
from django.utils import timezone

class SignedUp(models.Model):
    first_name= models.CharField(max_length=100, blank=False)
    last_name= models.CharField(max_length=100, blank=False)
    contact_email= models.EmailField(max_length=150, blank=False)
    contact_phone= models.CharField(max_length=13, blank=False)

    single_day_pass = models.CharField(max_length=100, blank=True, null=True)
    weekend_pass = models.CharField(max_length=100, blank=True, null=True)
    single_day_pass_normal = models.CharField(max_length=100, blank=True, null=True)
    weekend_pass_normal = models.CharField(max_length=100, blank=True, null=True)

    CHOICES = (('yes', 'Yes',), ('no', 'No',),)
    beeclub_asso = models.CharField(max_length=10, choices=CHOICES, blank=False)

    which_club= models.CharField(max_length=150, blank=True, null=True)

    CHOICES2 = (('my bee club', 'My bee club',), ('email newsletter', 'Email newsletter',),
                ('word of mouth', 'Word of mouth',), ('facebook', 'Facebook',),
                ('advertsment', 'Advertsment',),('other', 'Other',),)
    event = models.CharField(max_length=100, choices=CHOICES2, blank=True)

    dietary = models.CharField(max_length=150, blank=True, null=True)
    mailchimp_list = models.CharField(max_length=150, blank=True)
    paid = models.BooleanField(blank=True, default=False)
    signup_date = models.DateTimeField(default=timezone.now, blank=True, null=True,editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.first_name
