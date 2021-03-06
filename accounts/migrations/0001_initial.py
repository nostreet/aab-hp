# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 10:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daca', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=100)),
                ('committee', models.CharField(choices=[('President', 'President'), ('Vize-President', 'Vize-President'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Librarian', 'Librarian'), ('Web Master', 'Web Master'), ('Board Member', 'Board Member'), ('Member', 'Member')], default='Member', max_length=30)),
                ('city', models.CharField(default='', max_length=75)),
                ('mobile', models.CharField(default='', max_length=16)),
                ('experience', models.IntegerField(default='0')),
                ('profile_picture', easy_thumbnails.fields.ThumbnailerImageField(blank=True, default='/placeholder/neutral3.png', upload_to='profile_pics')),
                ('joined_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
