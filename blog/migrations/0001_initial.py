# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='news-images')),
                ('file2', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='news-images')),
                ('file3', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='news-images')),
                ('file4', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='news-images')),
                ('file5', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='news-images')),
                ('file6', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='news-images')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.Post'),
        ),
    ]
