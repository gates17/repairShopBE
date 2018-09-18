# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, mixins
from django.shortcuts import render
from .models import Reparacao
from .serializer import ReparacaoSerializer
from django.db.models import Q


class ReparacaoCreateView(generics.CreateAPIView):
    serializer_class = ReparacaoSerializer



class ReparacaoListView(generics.ListAPIView):
    serializer_class = ReparacaoSerializer
    lookup_field = 'id'


    def get_queryset(self):
        qs = Reparacao.objects.all();
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query).distinct()
            )
        return qs



class ReparacaoUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = ReparacaoSerializer

    def get_queryset(self):
        qs = Reparacao.objects.all();
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query).distinct()
            )
        return qs



class ReparacaoDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ReparacaoSerializer

    def get_queryset(self):
        return Reparacao.objects.all();



class ReparacaoDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = ReparacaoSerializer

    def get_queryset(self):
        return Reparacao.objects.all();


# Create your views here.
"""
class CategoryAPIView(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView
    lookup_field            = 'id' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = CategorySerializer
    #queryset                = BlogPost.objects.all()

    def get_queryset(self):
        qs = Category.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(name__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save()#user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    #pass
    lookup_field='id'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all();

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
"""