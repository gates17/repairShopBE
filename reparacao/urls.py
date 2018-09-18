from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReparacaoCreateView, ReparacaoDeleteView, ReparacaoDetailView, ReparacaoListView, ReparacaoUpdateView

#from django.contrib import admin

urlpatterns = [
    url(r'^$', ReparacaoListView.as_view(), name="reparacao_list"),
    url(r'^create/$', ReparacaoCreateView.as_view(), name="reparacao_create"),
    url(r'^update/(?P<id>\d+)/$', ReparacaoUpdateView.as_view(), name="reparacao_update"),
    url(r'^detail/(?P<id>\d+)/$', ReparacaoDetailView.as_view(), name="reparacao_detail"),
    url(r'^delete/(?P<id>\d+)/$', ReparacaoDeleteView.as_view(), name="reparacao_delete"),
]
