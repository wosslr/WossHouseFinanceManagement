from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    if request.method == 'GET':
        return HttpResponse('This is GET')
    else:
        return HttpResponse('This is POST')
