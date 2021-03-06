# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-05 13:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=500)),
                ('artist', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=1000)),
                ('album_logo', models.FileField(upload_to='', verbose_name=2000)),
                ('is_public', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SongList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=200)),
                ('song_file', models.FileField(max_length=1000, upload_to='')),
                ('is_public', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.AlbumList')),
            ],
        ),
    ]
