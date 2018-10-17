# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.urls import reverse
from rest_framework.reverse import reverse as reparacao_reverse
from decimal import Decimal
from cliente.models import Cliente

# Create your models here.


class Reparacao(models.Model):
    id = models.AutoField(primary_key=True)
    name_id = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_completed = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10 ,decimal_places=3, default=Decimal('0.00'))
    budget= models.DecimalField(max_digits=10 ,decimal_places=2, default=Decimal('0.00'))
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    materials = models.TextField(null=True, blank=True)
    pago= models.BooleanField(default=False)

    faturado= models.BooleanField(default=False)
    foto = models.CharField(max_length=255,blank=True, null=True)
    #foto = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return str(self.id)

    #blog property
    @property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'

    def get_reparacao_url(self, request=None):
        return reparacao_reverse("reparacao:reparacao_list",  request=request)
