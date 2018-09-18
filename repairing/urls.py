from django.conf.urls import url
from .views import RepairingRUDView,RepairingAPIView


urlpatterns = [
    url(r'^$', RepairingAPIView.as_view(), name='repairing-list'),
    url(r'^(?P<id>\d+)/$', RepairingRUDView.as_view(), name='repairing_rud_post')
]