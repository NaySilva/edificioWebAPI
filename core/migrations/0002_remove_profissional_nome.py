# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-07 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profissional',
            name='nome',
        ),
    ]