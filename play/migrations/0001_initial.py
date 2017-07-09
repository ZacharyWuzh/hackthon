# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 18:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('time', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('target_num_participants', models.IntegerField()),
                ('num_of_participants', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'plays',
            },
        ),
    ]
