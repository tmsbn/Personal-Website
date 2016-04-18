from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    json = open('sampledata/data/data.json')
    return HttpResponse(json)
