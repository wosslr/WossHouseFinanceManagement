from django.forms import ModelForm
from .models import AccountingDocumentHeader, AccountingDocumentItem
from django.forms.models import inlineformset_factory
from datetimewidget.widgets import DateTimeWidget
from .constants import dateTimeOptions


class AccountingDocumentForm(ModelForm):
    class Meta:
        model = AccountingDocumentHeader
        fields = ['creation_date', 'creator', 'comment']
        widgets = {
            'creation_date': DateTimeWidget(options=dateTimeOptions)
        }


AccountingDocumentItemFormSet = inlineformset_factory(model=AccountingDocumentItem,
                                                      parent_model=AccountingDocumentHeader,
                                                      form=AccountingDocumentForm,
                                                      fields=['dc_indicator', 'amount', 'account', 'comment'],
                                                      extra=2)