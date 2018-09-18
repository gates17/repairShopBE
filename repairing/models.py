# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.db import models
from django.urls import reverse
from rest_framework.reverse import reverse as repairing_reverse
# Create your models here.

class Repairing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=1024, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    #blog property
    @property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'

    def get_repairing_url(self, request=None):
        return repairing_reverse("repairing:repairing_rud_post", kwargs={'id': self.id}, request=request)