# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-07 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_sala_andar'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='andar',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
