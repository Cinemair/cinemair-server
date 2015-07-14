# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20150714_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tmdb_info',
            field=django_pgjson.fields.JsonBField(blank=True, verbose_name='themoviedb info', null=True),
        ),
    ]
