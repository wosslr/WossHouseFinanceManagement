from django.shortcuts import render, get_object_or_404
from .models import AccountingDocumentHeader

# Create your views here.


def index(request):
    account_doc_list = AccountingDocumentHeader.objects.order_by('-creation_date')
    context = {
        'account_doc_list': account_doc_list
    }
    return render(request=request, template_name='housefinance/index.html', context=context)


def detail(request, accountingDocumentID):
    account_doc = get_object_or_404(AccountingDocumentHeader, pk=accountingDocumentID)
    return render(request, template_name='housefinance/detail.html', context={'account_doc': account_doc})