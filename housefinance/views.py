from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import AccountingDocumentHeader

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'housefinance/index1.html'
    context_object_name = 'account_doc_list'

    def get_queryset(self):
        return AccountingDocumentHeader.objects.order_by('-creation_date')


class DetailView(generic.DetailView):
    model = AccountingDocumentHeader
    context_object_name = 'account_doc'
    template_name = 'housefinance/detail.html'