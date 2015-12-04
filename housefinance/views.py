from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

import json

from .models import AccountingDocumentHeader, AccountingDocumentItem

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'housefinance/index.html'
    context_object_name = 'account_doc_list'

    def get_queryset(self):
        return AccountingDocumentHeader.objects.order_by('-creation_date')


class DetailView(generic.DetailView):
    model = AccountingDocumentHeader
    context_object_name = 'account_doc'
    template_name = 'housefinance/detail.html'


class ChartSpendView(generic.TemplateView):
    template_name = 'housefinance/chart_spend.html'


def chart_spend_data(request):
    acc_doc_items = AccountingDocumentItem.objects.all()
    result = []
    for acc_doc_item in acc_doc_items:
        result.append(json.dumps({'y': acc_doc_item.amount.__float__()}))
    return HttpResponse(result)
