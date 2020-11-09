# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 12:59
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(null=True)),
            ],
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('number_of_pages', models.IntegerField()),
            ],
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='searchtests.Book')),
                ('setting', models.CharField(max_length=255)),
                ('protagonist', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='searchtests.Character')),
            ],
            bases=('searchtests.book',),
        ),
        migrations.CreateModel(
            name='ProgrammingGuide',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='searchtests.Book')),
                ('programming_language', models.CharField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('rs', 'Rust')], max_length=255)),
            ],
            bases=('searchtests.book',),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='searchtests.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='character',
            name='novel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='searchtests.Novel'),
        ),
    ]
