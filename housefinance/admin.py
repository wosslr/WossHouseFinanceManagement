from django.contrib import admin
from .models import User, Account, AccountingDocumentHeader, AccountingDocumentItem
# Register your models here.


class AccountingDocumentAdmin(admin.ModelAdmin):
    fields = ['creation_date', 'creator', 'comment']


admin.site.register(AccountingDocumentHeader, AccountingDocumentAdmin)
admin.site.register(User)
admin.site.register(Account)
