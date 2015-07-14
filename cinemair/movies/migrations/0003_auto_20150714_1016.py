# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_film_mdb_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='mdb_id',
            new_name='tmdb_id',
        ),
    ]
