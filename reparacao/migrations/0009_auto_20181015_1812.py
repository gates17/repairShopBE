# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-15 18:12
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparacao', '0008_reparacao_faturado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reparacao',
            name='tlf',
        ),
        migrations.AddField(
            model_name='reparacao',
            name='weight',
            field=models.DecimalField(decimal_places=3, default=Decimal('0.00'), max_digits=10),
        ),
    ]
