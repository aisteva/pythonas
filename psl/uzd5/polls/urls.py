from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.index, name='index'),
    #"ex:"/polls/5/"
    url(r'^(?P<aktas_id>[0n9]+)/$', views.detail, name='detail'),
    #"ex:"/polls/5/results/"
    url(r'^(?P<aktas_id>[0n9]+)/results/$', views.results, name='results'),]
