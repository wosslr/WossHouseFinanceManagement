from django.contrib import admin
from .models import User, Account, AccountingDocumentHeader, AccountingDocumentItem
# Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(AccountingDocumentHeader)
admin.site.register(AccountingDocumentItem)
