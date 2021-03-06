from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField

from django.utils import timezone
#update profile
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save


# User._meta.get_field('email').__dict__['_unique'] = True

class UserProfileInfo(models.Model):

    TYPE_CHOICES = (
       ('yes', 'yes'),
       ('no', 'no'),
       )
    POSITION_CHOICES = (
        ('President', 'President'),
        ('Vize-President', 'Vize-President'),
        ('Secretary', 'Secretary'),
        ('Treasurer', 'Treasurer'),
        ('Librarian', 'Librarian'),
        ('Web Master', 'Web Master'),
        ('Board Member', 'Board Member'),
        ('Member', 'Member'),
    )
    daca = models.CharField(max_length=100, choices=TYPE_CHOICES, default="no")
    committee  = models.CharField(max_length=30, choices=POSITION_CHOICES, default="Member")

    user = models.OneToOneField(User)
    city = models.CharField(max_length=75, blank=False, default='')
    mobile = models.CharField(max_length=16,blank=False, default='')
    experience = models.IntegerField(blank=False, default='0')
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_picture = ThumbnailerImageField(upload_to='profile_pics',blank=True,
                                            resize_source=dict(size=(550, 700)))
    joined_date = models.DateTimeField(default=timezone.now, blank=True, null=True,editable=False)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
         return self.user.first_name + " " + self.user.last_name

    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = UserProfileInfo(user=user)
            user_profile.save()
            post_save.connect(create_profile, sender=User)
