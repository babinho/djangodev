from django.shortcuts import render
from django.contrib.auth import views, logout
from .models import Nalog
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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
