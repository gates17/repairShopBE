# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-17 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('reparacao', '0011_auto_20181017_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reparacao',
            name='name',
        ),
        migrations.AddField(
            model_name='reparacao',
            name='name_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]
