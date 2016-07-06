# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_tmdb_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tmdb_videos',
            field=django_pgjson.fields.JsonBField(null=True, blank=True, verbose_name='themoviedb videos'),
        ),
    ]
