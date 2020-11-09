# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-26 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0046_contact_registration_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactgroup',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_groups', to='shuup.Shop', verbose_name='shop'),
        ),
    ]
