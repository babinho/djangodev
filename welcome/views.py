import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from django.http import JsonResponse
from . import database
from .models import PageView


# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

def getNalog(request):
    data = {
       'some_var_1': 'foo',
       'some_var_2': 'bar'
    }
    return JsonResponse(data)

def servisapp(request):
    return render(request, "welcome/servisapp.html")