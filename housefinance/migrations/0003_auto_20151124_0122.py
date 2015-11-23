# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housefinance', '0002_auto_20151124_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='accountingdocumentheader',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='accountingdocumentitem',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
