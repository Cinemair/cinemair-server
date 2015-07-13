# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='mdb_id',
            field=models.IntegerField(null=True, verbose_name='themoviedb id', blank=True),
        ),
    ]
