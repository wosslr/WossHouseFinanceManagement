# encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as SysUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=SysUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=10, blank=True)
    sys_user = models.OneToOneField(SysUser, blank=True)
    family = models.ForeignKey(Family, related_name='members')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Account(models.Model):
    ACCOUNT_TYPE_OPTIONS = (
        ('ZC', '资产'),
        ('CB', '成本'),
        ('FY', '费用'),
        ('FZ', '负债'),
        ('SR', '收入'),
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_OPTIONS)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    creator = models.ForeignKey(Member, verbose_name='创建人')

    def __str__(self):
        return self.name


class AccountingDocumentHeader(models.Model):
    creation_date = models.DateTimeField("记账日期")
    creator = models.ForeignKey(Member, verbose_name='创建人')
    comment = models.TextField(blank=True, verbose_name='备注')

    def __str__(self):
        return self.creation_date.date().__str__() + ' ' + self.id.__str__() + ' ' + self.comment

    def get_total_amount(self):
        total_amount = 0
        for acc_doc_item in self.accountingdocumentitem_set.all():
            total_amount += acc_doc_item.amount
        return total_amount

    get_total_amount.short_description = '金额'


class AccountingDocumentItem(models.Model):
    DEBIT_CREDIT_INDICATOR_OPTIONS = (
        ('J', '借方'),
        ('D', '贷方'),
    )
    dc_indicator = models.CharField(max_length=1, choices=DEBIT_CREDIT_INDICATOR_OPTIONS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    document_header = models.ForeignKey(AccountingDocumentHeader)
    account = models.ForeignKey(Account)
    comment = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.document_header.__str__() + ' ' + self.id.__str__()
