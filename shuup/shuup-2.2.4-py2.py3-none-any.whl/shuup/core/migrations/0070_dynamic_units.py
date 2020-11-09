# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-23 12:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
from shuup.core.utils.units import get_shuup_volume_unit
import shuup.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0069_shop_supplier_service_providers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='depth',
            field=shuup.core.fields.MeasurementField(decimal_places=9, default=0, help_text='Set the measured depth or length of your product or product packaging. This will provide customers with the product size and help with calculating shipping costs.', max_digits=36, unit=settings.SHUUP_LENGTH_UNIT, verbose_name='depth ({})'.format(settings.SHUUP_LENGTH_UNIT)),
        ),
        migrations.AlterField(
            model_name='product',
            name='gross_weight',
            field=shuup.core.fields.MeasurementField(decimal_places=9, default=0, help_text='Set the measured gross weight of your product WITH its packaging. This will help with calculating shipping costs.', max_digits=36, unit=settings.SHUUP_MASS_UNIT, verbose_name='gross weight ({})'.format(settings.SHUUP_MASS_UNIT)),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=shuup.core.fields.MeasurementField(decimal_places=9, default=0, help_text='Set the measured height of your product or product packaging. This will provide customers with the product size and help with calculating shipping costs.', max_digits=36, unit=settings.SHUUP_LENGTH_UNIT, verbose_name='height ({})'.format(settings.SHUUP_LENGTH_UNIT)),
        ),
        migrations.AlterField(
            model_name='product',
            name='net_weight',
            field=shuup.core.fields.MeasurementField(decimal_places=9, default=0, help_text="Set the measured weight of your product WITHOUT its packaging. This will provide customers with the actual product's weight.", max_digits=36, unit=settings.SHUUP_MASS_UNIT, verbose_name='net weight ({})'.format(settings.SHUUP_MASS_UNIT)),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=shuup.core.fields.MeasurementField(decimal_places=9, default=0, help_text='Set the measured width of your product or product packaging. This will provide customers with the product size and help with calculating shipping costs.', max_digits=36, unit=settings.SHUUP_LENGTH_UNIT, verbose_name='width ({})'.format(settings.SHUUP_LENGTH_UNIT)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='volume',
            field=shuup.core.fields.MeasurementField(decimal_places=9, default=0, max_digits=36, unit=get_shuup_volume_unit(), verbose_name='volume ({})'.format(get_shuup_volume_unit())),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='weight',
            field=shuup.core.fields.MeasurementField(decimal_places=9, default=0, max_digits=36, unit=settings.SHUUP_MASS_UNIT, verbose_name='weight ({})'.format(settings.SHUUP_MASS_UNIT)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='unit_volume',
            field=shuup.core.fields.MeasurementField(decimal_places=9, default=0, max_digits=36, unit=get_shuup_volume_unit(), verbose_name='unit volume ({})'.format(get_shuup_volume_unit())),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='unit_weight',
            field=shuup.core.fields.MeasurementField(decimal_places=9, default=0, max_digits=36, unit=settings.SHUUP_MASS_UNIT, verbose_name='unit weight ({})'.format(settings.SHUUP_MASS_UNIT)),
        ),
        migrations.AlterField(
            model_name='weightbasedpricerange',
            name='max_value',
            field=shuup.core.fields.MeasurementField(blank=True, decimal_places=9, default=0, help_text='The maximum weight before this price no longer applies.', max_digits=36, null=True, unit=settings.SHUUP_MASS_UNIT, verbose_name='max weight ({})'.format(settings.SHUUP_MASS_UNIT)),
        ),
        migrations.AlterField(
            model_name='weightbasedpricerange',
            name='min_value',
            field=shuup.core.fields.MeasurementField(blank=True, decimal_places=9, default=0, help_text='The minimum weight for this price to apply.', max_digits=36, null=True, unit=settings.SHUUP_MASS_UNIT, verbose_name='min weight ({})'.format(settings.SHUUP_MASS_UNIT)),
        ),
    ]
