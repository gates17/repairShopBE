from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClienteCreateView, ClienteDeleteView, ClienteDetailView, ClienteListView, ClienteUpdateView

#from django.contrib import admin

urlpatterns = [
    url(r'^$', ClienteListView.as_view(), name="cliente_list"),
    url(r'^create/$', ClienteCreateView.as_view(), name="cliente_create"),
    url(r'^update/(?P<id>\d+)/$', ClienteUpdateView.as_view(), name="cliente_update"),
    url(r'^detail/(?P<id>\d+)/$', ClienteDetailView.as_view(), name="cliente_detail"),
    url(r'^delete/(?P<id>\d+)/$', ClienteDeleteView.as_view(), name="cliente_delete"),
]
