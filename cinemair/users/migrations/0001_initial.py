# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, help_text='Required. 255 characters or fewer. Letters, numbers and /./-/_ characters', validators=[django.core.validators.RegexValidator(re.compile('^[\\w.-]+$', 32), 'Enter a valid username.', 'invalid')], unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=255, verbose_name='email address', unique=True)),
                ('full_name', models.CharField(max_length=256, verbose_name='full name', blank=True)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'ordering': ['username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
