# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 11:19
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0029_auto_20180320_0838'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='map',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
