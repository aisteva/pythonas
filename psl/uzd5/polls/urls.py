from django.conf.urls import url
from . import views
from polls.views import AktasCreate

urlpatterns = [url(r'^$', views.index, name='index'),
    #"ex:"/polls/5/"
    url(r'^(?P<aktas_id>[0-9]+)/$', views.detail, name='detail'),
    #"ex:"/polls/add/"
    url(r'aktas/add/$', views.AktasCreate.as_view(), name='aktas-add'),]
    #url(r'^(?P<aktas_id>[0-9]+)/results/$', views.results, name='results'),]
