# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0002_auto_20150713_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinema',
            old_name='adress',
            new_name='address',
        ),
    ]
