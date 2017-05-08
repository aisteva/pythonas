from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Pirmas kažkam skirtas puslapis - polls.")
# Create your views here.
