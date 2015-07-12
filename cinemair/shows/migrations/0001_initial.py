# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0001_initial'),
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='datetime')),
                ('cinema', models.ForeignKey(related_name='shows', verbose_name='cinema', to='cinemas.Cinema')),
                ('film', models.ForeignKey(related_name='shows', verbose_name='film', to='films.Film')),
            ],
            options={
                'verbose_name_plural': 'shows',
                'verbose_name': 'show',
            },
        ),
    ]
