# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-17 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reparacao', '0010_reparacao_nome2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reparacao',
            name='nome2',
        ),
        migrations.AddField(
            model_name='reparacao',
            name='pago',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reparacao',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]
