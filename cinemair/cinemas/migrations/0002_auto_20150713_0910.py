# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='adress',
            field=models.TextField(verbose_name='address', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='city',
            field=models.CharField(verbose_name='city', null=True, max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='country',
            field=models.CharField(verbose_name='country', null=True, max_length=500, blank=True),
        ),
    ]
