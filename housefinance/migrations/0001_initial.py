# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('account_name', models.CharField(max_length=50)),
                ('account_type', models.CharField(max_length=10)),
                ('account_balance', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='AccountingDocumentHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('creation_date', models.DateTimeField(verbose_name='Document Date')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AccountingDocumentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('dc_indicator', models.CharField(max_length=1)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('comment', models.TextField()),
                ('account', models.ForeignKey(to='housefinance.Account')),
                ('document_header', models.ForeignKey(to='housefinance.AccountingDocumentHeader')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_role', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='accountingdocumentheader',
            name='creator',
            field=models.ForeignKey(to='housefinance.User'),
        ),
    ]
