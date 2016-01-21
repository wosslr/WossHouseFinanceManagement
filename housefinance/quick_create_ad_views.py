from . import views


class QuickViewSpend(views.AccountingDocumentCreateView):
    template_name = 'housefinance/accounting_document/acc_doc_quick_create_spend.html'
