# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='age',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dog',
            name='habit',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dog',
            name='live',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
