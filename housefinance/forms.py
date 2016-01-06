from django.forms import ModelForm
from .models import AccountingDocumentHeader, AccountingDocumentItem
from django.forms.models import inlineformset_factory


class AccountingDocumentForm(ModelForm):
    class Meta:
        model = AccountingDocumentHeader
        fields = ['creation_date', 'creator', 'comment']


AccountingDocumentItemFormSet = inlineformset_factory(model=AccountingDocumentItem,
                                                      parent_model=AccountingDocumentHeader,
                                                      form=AccountingDocumentForm,
                                                      fields=['dc_indicator', 'amount', 'account', 'comment'],
                                                      extra=2)