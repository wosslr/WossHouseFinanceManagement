# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('ZC', '资产'), ('CB', '成本'), ('FY', '费用'), ('FZ', '负债'), ('SR', '收入')], max_length=10)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='AccountingDocumentHeader',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(verbose_name='记账日期')),
                ('comment', models.TextField(blank=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='AccountingDocumentItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('dc_indicator', models.CharField(choices=[('J', '借方'), ('D', '贷方')], max_length=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('account', models.ForeignKey(to='housefinance.Account')),
                ('document_header', models.ForeignKey(to='housefinance.AccountingDocumentHeader')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(blank=True, max_length=10)),
                ('family', models.ForeignKey(related_name='members', to='housefinance.Family')),
                ('sys_user', models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='accountingdocumentheader',
            name='creator',
            field=models.ForeignKey(verbose_name='创建人', to='housefinance.Member'),
        ),
        migrations.AddField(
            model_name='account',
            name='creator',
            field=models.ForeignKey(verbose_name='创建人', to='housefinance.Member'),
        ),
    ]
