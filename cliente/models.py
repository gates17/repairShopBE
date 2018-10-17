# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.urls import reverse
from rest_framework.reverse import reverse as cilente_reverse
from decimal import Decimal
# Create your models here.


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=1024, null=True,blank=True)
    zip_code = models.CharField(max_length=16,null=True, blank=True)
    localidade = models.CharField(max_length=16, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    tlf = models.CharField(max_length=15, null=True, blank=True)
    total_spent_by_client = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return str(self.name)

    #blog property
    @property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'

    def get_cliente_url(self, request=None):
        return cilente_reverse("cliente:cliente_list",  request=request)