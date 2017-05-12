from django.shortcuts import render
from django.http import HttpResponse
from .models import Aktas
from django.template import loader
from django.http import Http404

def index(request):
    latest_aktas_list = Aktas.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    #context = { 'latest_aktas_list':latest_aktas_list, }
#output = ','.join([a.pavadinimas for a in latest_aktas_list])
    return render(request, 'polls/index.html', context)
	
def detail(request, aktas_id):
    return HttpResponse("Matomas klausimas, kurio id {0}.".format(aktas_id))
	
	
def results(request, aktas_id):
    response ="Klausimo {0} rezultatai."
    return HttpResponse(response.format(aktas_id))
# Create your views here.
