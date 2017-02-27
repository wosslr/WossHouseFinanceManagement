from django.contrib.auth.models import User, Group
from .models import Account, AccountingDocumentHeader, AccountingDocumentItem
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('account_name', 'account_type', 'account_balance')


class AccountingDocumentHeaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountingDocumentHeader
        fields = ('creation_date', 'creator', 'comment')


class AccountingDocumentItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountingDocumentItem
        fields = ('dc_indicator', 'amount', 'document_header', 'account', 'comment')
