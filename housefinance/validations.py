from .models import AccountingDocumentHeader, AccountingDocumentItem
from decimal import Decimal


class AccountingDocumentValidation:

    def is_document_consistent(self, **kwargs):
        accounting_document = AccountingDocumentHeader()
        changed_objects = []
        deleted_objects = []
        new_objects = []
        amount_j = Decimal(0)
        amount_d = Decimal(0)
        for key, value in kwargs.items():
            if key == 'accounting_document':
                accounting_document = value
            elif key == 'changed_objects':
                changed_objects = value
            elif key == 'deleted_objects':
                deleted_objects = value
            elif key == 'new_objects':
                new_objects = value

        # accounting_document_items = accounting_document.accountingdocumentitem_set.all()
        # for index, acc_item in enumerate(accounting_document_items):
        #     for acc_item_del in deleted_objects:
        #         if acc_item.id == acc_item_del.id:
        #             del accounting_document_items[index]

        for acc_item_chg in changed_objects:
            if acc_item_chg.dc_indicator == 'J':
                amount_j += acc_item_chg.amount
            else:
                amount_d += acc_item_chg.amount

        for acc_item_new in new_objects:
            if acc_item_new.dc_indicator == 'J':
                amount_j += acc_item_new.amount
            else:
                amount_d += acc_item_new.amount

        for acc_item_del in deleted_objects:
            if acc_item_del.dc_indicator == 'J':
                amount_j -= acc_item_del.amount
            else:
                amount_d -= acc_item_del.amount

        return amount_d == amount_j and amount_j != 0

