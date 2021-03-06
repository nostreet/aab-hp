# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('storyline', models.TextField()),
                ('book_cover', easy_thumbnails.fields.ThumbnailerImageField(blank=True, default='/placeholder/neutral_book_cover.png', upload_to='book_cover')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
