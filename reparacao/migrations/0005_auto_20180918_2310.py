# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 23:10
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparacao', '0004_auto_20180918_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='reparacao',
            name='budget',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AddField(
            model_name='reparacao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='reparacao',
            name='materials',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reparacao',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AddField(
            model_name='reparacao',
            name='tlf',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
