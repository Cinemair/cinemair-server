# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'verbose_name_plural': 'shows', 'ordering': ['datetime', 'cinema', 'id'], 'verbose_name': 'show'},
        ),
    ]
