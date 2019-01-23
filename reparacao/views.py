# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Reparacao,Cliente
from django.core.paginator import Paginator
import sys, os
from decimal import Decimal

from rest_framework import generics
from .serializer import *
from django.db.models import Q

from datetime import date

from rest_framework import status
from rest_framework.response import Response
from .pagination import PostPageNumberPagination #PostLimitOffSetPagination
from .calc_rules import calc_total


class ReparacaoCreateView(generics.CreateAPIView):
    model = Reparacao
    serializer_class = ReparacaoCreateSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        total_dict = {}
        total_dict = calc_total(self.request.data)
        request.data['total_to_pay'] = total_dict['total_to_pay']
        request.data['total_to_pay_with_tax'] = total_dict['total_to_pay_with_tax']
        request.data['tax_to_pay'] = total_dict['tax_to_pay']
        print(request.data)
        if not request.data['date_completed'] or request.data['date_completed']=='':
            request.data['date_completed']=None
        if not request.data['price']:
            request.data['price']=0
        if not request.data['budget']:
            request.data['budget'] = 0
        if not request.data['weigth']:
            request.data['weigth'] = 0
        if not request.data['pagamento_parcial']:
            request.data['pagamento_parcial'] = 0
        if not request.data['discount']:
            request.data['discount'] = 0
        serializer = self.get_serializer(data=request.data)
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
            if query == 'today':
                qs = qs.filter(
                    #Q(date_created='2018-09-26')).distinct()
                    Q(date_created=date.today())).distinct()
                return qs
            if query =='list':
                print(self.pagination_class)
                list_string=(self.request.GET.get("qp"))
                if list_string:
                    self.pagination_class=None
                list_to_print= [int(s) for s in list_string.split(',')]
                qs = qs.filter(id__in=list_to_print)
                return qs
            if query =='day':
                data=self.request.GET.get("qd")
                if data=='null':
                    data=None
                if data:
                    qs = qs.filter(date_created=data).distinct()
                else:
                    qs = qs.filter(Q(date_created=date.today())).distinct()
                return qs

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

    '''self
    'allowed_methods', 'args', 'as_view', 'authentication_classes', 'check_object_permissions', 'check_permissions', 
    'check_throttles', 'content_negotiation_class', 'default_response_headers', 'determine_version', 'dispatch', 
    'filter_backends', 'filter_queryset', 'finalize_response', 'format_kwarg', 'get_authenticate_header', 'get_authenticators', 
    'get_content_negotiator', 'get_exception_handler', 'get_exception_handler_context', 'get_format_suffix', 'get_object', 
    'get_paginated_response', 'get_parser_context', 'get_parsers', 'get_permissions', 'get_queryset', 'get_renderer_context', 
    'get_renderers', 'get_serializer', 'get_serializer_class', 'get_serializer_context', 'get_throttles', '
    get_view_description', 'get_view_name', 'handle_exception', 'headers', 'http_method_names', 'http_method_not_allowed', 
    'initial', 'initialize_request', 'kwargs', 'lookup_field', 'lookup_url_kwarg', 'metadata_class', 'options', 
    'paginate_queryset', 'pagination_class', 'paginator', 'parser_classes', 'partial_update', 'patch', 'perform_authentication',
    'perform_content_negotiation', 'perform_update', 'permission_classes', 'permission_denied', 'put', 'queryset', 
    'raise_uncaught_exception', 'renderer_classes', 'request', 'schema', 'serializer_class', 'settings', 'throttle_classes', 
    'throttled', 'update', 'versioning_class'
    '''

    def get_queryset(self):
        try:
            if(self.request.data):
                total_dict ={}
                total_dict= calc_total(self.request.data)
                print(total_dict)
                print(self.request.data['tax'])
                self.request.data['total_to_pay']=total_dict['total_to_pay']
                self.request.data['total_to_pay_with_tax']=total_dict['total_to_pay_with_tax']
                self.request.data['tax_to_pay']=total_dict['tax_to_pay']
                print(total_dict['total_to_pay'])
                print(total_dict['total_to_pay_with_tax'])
                print(total_dict['tax_to_pay'])
                serializer = self.get_serializer(data=self.request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

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


