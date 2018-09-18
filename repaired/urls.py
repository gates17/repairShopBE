from django.conf.urls import url
from .views import RepairedRUDView,RepairedAPIView


urlpatterns = [
    url(r'^$', RepairedAPIView.as_view(), name='repaired-list'),
    url(r'^(?P<id>\d+)/$', RepairedRUDView.as_view(), name='repaired_rud_post')
]