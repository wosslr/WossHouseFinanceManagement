from django.contrib import admin
from .models import User, Account, AccountingDocumentHeader, AccountingDocumentItem
from decimal import Decimal
from .validations import AccountingDocumentValidation
from django.contrib import messages


# Register your models here.


class AccountingDocumentItemInline(admin.TabularInline):
    model = AccountingDocumentItem
    extra = 0


class AccountingDocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Header Information', {'fields': ['creation_date', 'creator']}),
        ('Comment', {'fields': ['comment']})
    ]
    inlines = [AccountingDocumentItemInline]
    list_display = ('creation_date', 'creator', 'comment')
    list_filter = ['creation_date']
    search_fields = ['comment']

    # def save_model(self, request, obj, form, change):
    #     print('------------>save model')
    #     amount_j, amount_d = Decimal(0), Decimal(0)
    #     for acc_doc_item in obj.accountingdocumentitem_set.all():
    #         if acc_doc_item.dc_indicator == 'J':
    #             amount_j += acc_doc_item.amount
    #         else:
    #             amount_d += acc_doc_item.amount
    #     print(amount_j, amount_d)
    #     if amount_d == amount_j:
    #         obj.save()

    def save_form(self, request, form, change):
        print('------------>save form')
        test = super(AccountingDocumentAdmin, self).save_form(request, form, change)
        for it in test.accountingdocumentitem_set.all():
            print(it)
        print(test)
        return test

    def save_formset(self, request, form, formset, change):
        print('------------>save formset')
        instances = formset.save(commit=False)
        acc_doc_valdt = AccountingDocumentValidation()
        if acc_doc_valdt.is_document_consistent(changed_objects=formset.changed_objects,
                                             deleted_objects=formset.deleted_objects, new_objects=formset.new_objects):
            messages.error(request, 'The document is inconsistent')


admin.site.register(AccountingDocumentHeader, AccountingDocumentAdmin)
admin.site.register(User)
admin.site.register(Account)
