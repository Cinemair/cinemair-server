# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_auto_20150712_2126'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('show', models.ForeignKey(to='shows.Show', verbose_name='show', related_name='events')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='events')),
            ],
            options={
                'ordering': ['user', 'show', 'id'],
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
