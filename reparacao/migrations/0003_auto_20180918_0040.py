# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparacao', '0002_auto_20180918_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparacao',
            name='date_completed',
            field=models.DateField(blank=True, null=True),
        ),
    ]