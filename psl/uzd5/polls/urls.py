from django.conf.urls import url
from . import views
from polls.views import AktasCreate, GeneratePDF


urlpatterns = [url(r'^$', views.index, name='index'),
    #"ex:"/polls/5/"
    url(r'a/(?P<aktas_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'p/(?P<aktas_id>[0-9]+)/$', views.detailPDF, name='detailPDF'),
    #"ex:"/polls/add/"
    url(r'aktas/add/$', views.AktasCreate.as_view(), name='aktas-add'),]
    #url(r'^(?P<aktas_id>[0-9]+)/results/$', views.results, name='results'),]
