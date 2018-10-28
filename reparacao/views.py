# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .models import Reparacao,Cliente
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
            request.data['budget'] = 0
        if not request.data['weigth']:
            request.data['weigth'] = 0
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ReparacaoListView(generics.ListAPIView):
    serializer_class = ReparacaoListSerializer
    lookup_field = 'id'
    pagination_class =  PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        qs = Reparacao.objects.all().filter(faturado=False).select_related('name_id').order_by('id')
        query = self.request.GET.get("q")

        if('all' in self.request.GET.values()):
            self.pagination_class = None
            query=self.request.GET.get("qc")
            query=qs.filter(name_id=self.request.GET.get("qc"))
            return query

        for key in self.request.GET.iterkeys():  # "for key in request.GET" works too.
            # Add filtering logic here.
            valuelist = self.request.GET.getlist(key)
            if(valuelist[0] == 'asc'):
                qs = Reparacao.objects.all().order_by(key)

            if(valuelist[0] == 'desc'):
                qs = Reparacao.objects.all().order_by(('-'+key))

        dateStartQuery = self.request.GET.get("qdi")
        dateFinishQuery = self.request.GET.get("qdf")
        clientRelatedQuery = self.request.GET.get("qc")
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
        if clientRelatedQuery:
            qs = qs.filter(name_id=clientRelatedQuery)
        if query is not None:
            clientFilter = Cliente.objects.all().filter(name__icontains=query)
            if clientFilter:
                qs = qs.filter(
                    Q(name_id__in=clientFilter)
                ).distinct()
                return qs.order_by('name_id')
            qs = qs.filter(
                Q(name_id=id)
                | Q(id=query)
            ).distinct()
        return qs

class ReparacaoUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = ReparacaoUpdateSerializer

    def get_queryset(self):
        qs = Reparacao.objects.all().select_related('name_id');
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query).distinct()
            ).select_related('name_id')
        return qs

class ReparacaoDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ReparacaoDetailSerializer

    def get_queryset(self):
        return Reparacao.objects.all().select_related('name_id');

class ReparacaoDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = ReparacaoDeleteSerializer

    def get_queryset(self):
        return Reparacao.objects.all().select_related('name_id');


