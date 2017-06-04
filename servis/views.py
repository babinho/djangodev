from django.shortcuts import render
from django.contrib.auth import views, logout
from .models import Nalog
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

# Create your views here.

def getNalog(request):
	a = Nalog.objects.count()
	data = {
       'some_var_1': 'foo',
       'some_var_2': 'bar'
    }
	return JsonResponse(data)


def servisLogin(request):
    template_response = render(request, "login.html")
    data = {
       'some_var_1': 'foo',
       'some_var_2': 'bar',
    }
    # return JsonResponse(data)
    # Do something with `template_response`
    return template_response

@login_required
def servis(request):
    template_response = render(request, "servis.html")
    return template_response


def servisLogout(request):
    logout(request)
    template_response = render(request, "registration/login.html")
    return template_response

@login_required
def getNalogById(request):
  return response

@login_required
def saveNalog(request):
  return response


@login_required
def getNalogList(request):
    result = Nalog.objects.values()
    return JsonResponse({"data" : list(result)})
