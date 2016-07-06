# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20150714_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tmdb_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='themoviedb info'),
        ),
    ]
