from django.shortcuts import render
from django.template import loader
from collections import namedtuple
import json


def index(request):

    with open('resume/data/resume_data.json') as json_data:
        app_data = json.load(json_data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    print(app_data.summary.email)
    context = {
        'app_data': app_data

    }
    return render(request, 'resume/index.html', context)