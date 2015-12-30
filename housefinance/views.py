from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import AccountingDocumentHeader, AccountingDocumentItem

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'housefinance/index.html'
    context_object_name = 'account_doc_list'

    def get_queryset(self):
        return AccountingDocumentHeader.objects.order_by('-creation_date')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)


class DetailView(generic.DetailView):
    model = AccountingDocumentHeader
    context_object_name = 'account_doc'
    template_name = 'housefinance/detail.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(DetailView, self).dispatch(request, *args, **kwargs)


@login_required(login_url='/login/')
def chart_spend(request):
    acc_doc_items = AccountingDocumentItem.objects.filter(account__account_type='FY').order_by('document_header__creation_date')
    context = {'acc_doc_items': acc_doc_items}
    return render(request=request, template_name='housefinance/chart_spend.html', context=context)


@login_required(login_url='/login/')
def fibonacci(request, m):
    tm = int(m)
    context = {'fibonacci': fib(tm)}
    return render(request=request, template_name='housefinance/fibonacci.html', context=context)


def fib(m):
    n, a, b = 0, 0, 1
    y = float(0)
    result = []
    while n < m:
        # yield a
        a, b = b, a + b
        y = a / b
        result.append(y)
        n += 1
    return result
