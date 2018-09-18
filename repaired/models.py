# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from rest_framework.reverse import reverse as repaired_reverse

# Create your models here.


class Repaired(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=1024, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    #blog property
    @property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'

    def get_repaired_url(self, request=None):
        return repaired_reverse("repaired:repaired_rud_post", kwargs={'id': self.id}, request=request)
        #return product_reverse("product:product_rud_post", kwargs={'id': self.id}, request=request)