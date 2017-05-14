from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Aktas
from django.template import loader, Context
from django.http import Http404
from django.db.models import Sum
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.template.loader import get_template
from polls.utils import render_to_pdf #created in step 4

class AktasCreate(CreateView):
        model = Aktas
        fields = '__all__'
		
		
def index(request):
    latest_aktas_list = Aktas.objects.order_by('-data')[:5]
    template = loader.get_template('polls/index.html')
    context = { 'latest_aktas_list':latest_aktas_list, }
#output = ','.join([a.pavadinimas for a in latest_aktas_list])
    return render(request, 'polls/index.html', context)
	


def detail(request, aktas_id):
    aktas = get_object_or_404(Aktas, pk = aktas_id)
    total = aktas.vertybe.all().aggregate(Sum('suma'))
    return render(request, 'polls/detail.html', {'aktas': aktas, 'total': total})
	
	
def detailPDF(request, aktas_id):
    aktas = get_object_or_404(Aktas, pk = aktas_id)
    total = aktas.vertybe.all().aggregate(Sum('suma'))
    pdf = render_to_pdf('polls/detail.html', {'aktas': aktas, 'total': total})
    return HttpResponse(pdf, content_type = 'application/pdf')

	

# Create your views here.
