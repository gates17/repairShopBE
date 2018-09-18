# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from rest_framework import generics, mixins, permissions
from django.shortcuts import render
from .models import Repairing
from .serializer import RepairingSerializer
from django.db.models import Q

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.

class RepairingAPIView(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView
    lookup_field            = 'id' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = RepairingSerializer
    #permission_classes = (permissions.IsAdminUser)

    def get_queryset(self):
        qs = Repairing.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(name__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()#user=self.request.user)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class RepairingRUDView(generics.RetrieveUpdateDestroyAPIView):
    #pass
    lookup_field='id'
    serializer_class = RepairingSerializer
    #permission_classes = (permissions.IsAdminUser)

    def get_queryset(self):
        return Repairing.objects.all();

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
