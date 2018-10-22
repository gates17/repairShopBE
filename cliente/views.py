# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, mixins
from django.shortcuts import render
from .models import Cliente
from .serializer import ClienteSerializer
from django.db.models import Q
from rest_framework.response import Response
from .pagination import PostPageNumberPagination #PostLimitOffSetPagination


class ClienteCreateView(generics.CreateAPIView):
    serializer_class = ClienteSerializer

class ClienteListView(generics.ListAPIView):
    serializer_class = ClienteSerializer
    lookup_field = 'id'
    pagination_class =  PostPageNumberPagination


    def get_queryset(self):
        qs = Cliente.objects.all();
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query).distinct()
            )

        #total_spent = self.total_debt_by_client()
        #qs.annotate(total_debt_by_client=total_spent)
        return qs

class ClienteUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = ClienteSerializer

    def get_queryset(self):
        qs = Cliente.objects.all();
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query).distinct()
            )

        return qs

class ClienteDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.all();

class ClienteDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.all();