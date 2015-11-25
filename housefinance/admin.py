from django.contrib import admin
from .models import User, Account, AccountingDocumentHeader, AccountingDocumentItem
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


admin.site.register(AccountingDocumentHeader, AccountingDocumentAdmin)
admin.site.register(User)
admin.site.register(Account)
