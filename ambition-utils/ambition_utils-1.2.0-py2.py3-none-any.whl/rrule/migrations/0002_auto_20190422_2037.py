# Generated by Django 2.1.7 on 2019-04-22 20:37

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rrule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rrule',
            name='time_zone',
            field=timezone_field.fields.TimeZoneField(default='UTC'),
        ),
    ]
