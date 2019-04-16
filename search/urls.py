from django.conf.urls import url
from . import views
import bangla

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
    url(r'^custom/$', views.custom, name='custom')
];
