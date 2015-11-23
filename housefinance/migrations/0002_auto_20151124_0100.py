# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housefinance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_balance',
            field=models.DecimalField(max_digits=10, default=0, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='accountingdocumentheader',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='accountingdocumentitem',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(null=True, max_length=10),
        ),
    ]
