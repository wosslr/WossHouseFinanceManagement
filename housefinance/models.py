from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_role = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Account(models.Model):
    account_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=10, blank=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.account_name


class AccountingDocumentHeader(models.Model):
    creation_date = models.DateTimeField("Document Date")
    creator = models.ForeignKey(User)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.creation_date.__str__() + ' ' + self.id.__str__()


class AccountingDocumentItem(models.Model):
    dc_indicator = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    document_header = models.ForeignKey(AccountingDocumentHeader)
    account = models.ForeignKey(Account)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.document_header.__str__() + ' ' + self.id.__str__()