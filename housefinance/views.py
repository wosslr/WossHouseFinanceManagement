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


def chart_spend(request):
    acc_doc_items = AccountingDocumentItem.objects.filter(account__account_type='FY').order_by('document_header__creation_date')
    context = {'acc_doc_items': acc_doc_items}
    for acc_doc_item in acc_doc_items:
        print(acc_doc_item.document_header.comment)
        print(acc_doc_item.document_header.creation_date.month)
    return render(request=request, template_name='housefinance/chart_spend.html', context=context)
