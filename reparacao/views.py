# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .models import Reparacao
from .serializer import *
from django.db.models import Q

from django.core.paginator import Paginator


from rest_framework import status
from rest_framework.response import Response
from .pagination import PostPageNumberPagination #PostLimitOffSetPagination


class ReparacaoCreateView(generics.CreateAPIView):
    model = Reparacao
    serializer_class = ReparacaoCreateSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not request.data['date_completed'] or request.data['date_completed']=='':
            request.data['date_completed']=None
        if not request.data['price']:
            request.data['price']=0
        if not request.data['budget']:
            request.data['budget']=0
        print "POST"
        print request.data['faturado']
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ReparacaoListView(generics.ListAPIView):
    serializer_class = ReparacaoListSerializer
    lookup_field = 'id'
    pagination_class =  PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        qs = Reparacao.objects.all().filter(faturado=False).select_related('nome2')
        query = self.request.GET.get("q")
        dateStartQuery = self.request.GET.get("qdi")
        dateFinishQuery = self.request.GET.get("qdf")

        print dateStartQuery, dateFinishQuery,query
        if dateStartQuery:
            qs = qs.filter(
                Q(date_created__gte=dateStartQuery)
                #Q(date_completed__gte=dateStartQuery) |
                #Q(date_created__lte=dateFinishQuery) |
                #Q(date_completed__lte=dateFinishQuery)
            ).distinct()
        if dateFinishQuery:
            qs = qs.filter(
                #Q(date_created__gte=dateStartQuery) |
                #Q(date_completed__gte=dateStartQuery) |
                #Q(date_created__lte=dateFinishQuery) |
                Q(date_completed__lte=dateFinishQuery)
            ).distinct()
        if dateFinishQuery and dateStartQuery:
            qs = qs.filter(
                (Q(date_created__gte=dateStartQuery)& Q(date_completed__lte=dateFinishQuery))
            ).distinct()
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(id=query)

            ).distinct()


            # print page_list
        #return paginator.get_paginated_response(serializer.data)
        print qs.query
        return qs

class ReparacaoUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = ReparacaoUpdateSerializer

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
    serializer_class = ReparacaoDetailSerializer

    def get_queryset(self):
        return Reparacao.objects.all();

class ReparacaoDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = ReparacaoDeleteSerializer

    def get_queryset(self):
        return Reparacao.objects.all();


