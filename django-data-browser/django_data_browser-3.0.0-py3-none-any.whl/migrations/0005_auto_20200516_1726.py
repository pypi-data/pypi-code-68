# Generated by Django 2.0.13 on 2020-05-16 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data_browser", "0004_auto_20200501_0903"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="view",
            options={
                "permissions": [
                    ("make_view_public", "Can make a saved view publically available")
                ]
            },
        ),
    ]
