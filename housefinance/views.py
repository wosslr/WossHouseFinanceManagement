from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello you are in the index")

def detail(request, accountingDocumentID):
    response = "You're looking at the detail of accounting document %s."
    return HttpResponse(response % accountingDocumentID)

