from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.utils.urls import remove_query_param, replace_query_param
from rest_framework.response import Response
from collections import OrderedDict, namedtuple

class PostLimitOffSetPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 10

class PostPageNumberPagination(PageNumberPagination):
    page_size = 10
    display_page_controls = True



    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
            ('pages_list', self.get_html_context())
        ]))
