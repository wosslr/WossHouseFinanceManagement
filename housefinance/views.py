from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetimewidget.widgets import DateTimeWidget
from .constants import dateTimeOptions

from .forms import AccountingDocumentForm, AccountingDocumentItemFormSet
from .models import AccountingDocumentHeader, AccountingDocumentItem
from .validations import AccountingDocumentValidation
from .funs import fib


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'housefinance/index.html'
    context_object_name = 'account_doc_list'

    def get_queryset(self):
        return AccountingDocumentHeader.objects.order_by('-creation_date')

    @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)


class AccountingDocumentIndexView(generic.ListView):
    template_name = 'housefinance/accounting_document/index.html'
    context_object_name = 'account_doc_list'

    def get_queryset(self):
        return AccountingDocumentHeader.objects.order_by('-creation_date')

    @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(AccountingDocumentIndexView, self).dispatch(request, *args, **kwargs)


class AccountingDocumentDetailView(generic.DetailView):
    model = AccountingDocumentHeader
    context_object_name = 'account_doc'
    template_name = 'housefinance/accounting_document/detail.html'

    @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(AccountingDocumentDetailView, self).dispatch(request, *args, **kwargs)


class AccountingDocumentCreateView(generic.CreateView):
    model = AccountingDocumentHeader
    # fields = ['creation_date', 'creator', 'comment']
    form_class = AccountingDocumentForm
    template_name = 'housefinance/accounting_document/acc_doc_create.html'

    def get_context_data(self, **kwargs):
        context = super(AccountingDocumentCreateView, self).get_context_data(**kwargs)
        context['formset'] = AccountingDocumentItemFormSet(queryset=AccountingDocumentItem.objects.none())
        return context

    def get_form(self, form_class=None):
        form = super(AccountingDocumentCreateView, self).get_form(form_class)
        form.fields['creation_date'].widget = DateTimeWidget(options=dateTimeOptions)
        return form

    def post(self, request, *args, **kwargs):
        print('----> post in acc doc create')
        form = AccountingDocumentForm(request.POST)
        acc_doc_header = form.save(commit=False)
        formset = AccountingDocumentItemFormSet(request.POST, instance=acc_doc_header)
        context = {'form': form,
                   'formset': formset}
        if formset.is_valid():
            acc_doc_items = formset.save(commit=False)
            if not AccountingDocumentValidation().is_document_consistent(
                    request=request,
                    changed_objects=formset.changed_objects,
                    deleted_objects=formset.deleted_objects,
                    new_objects=formset.new_objects,
                    acc_doc_header=acc_doc_header
            ):
                # acc_doc_header.delete()
                return render(request, template_name='housefinance/accounting_document/acc_doc_create.html',
                              context=context)
            else:
                acc_doc_header = form.save(commit=True)
                acc_doc_items = formset.save(commit=True)
                print(acc_doc_header)
                print(acc_doc_items)
                return HttpResponseRedirect('/ffm/accounting_document')

    @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(AccountingDocumentCreateView, self).dispatch(request, *args, **kwargs)


@login_required(login_url='/account/login')
def chart_spend(request):
    acc_doc_items = AccountingDocumentItem.objects.filter(account__account_type='FY').order_by(
        'document_header__creation_date')
    context = {'acc_doc_items': acc_doc_items}
    return render(request=request, template_name='housefinance/chart_spend.html', context=context)


@login_required(login_url='/account/login')
def fibonacci(request, m):
    tm = int(m)
    context = {'fibonacci': fib(tm)}
    return render(request=request, template_name='housefinance/fibonacci.html', context=context)
