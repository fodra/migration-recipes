# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 07:49
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    Author = apps.get_model('rename_app', 'Author')
    Book = apps.get_model('rename_app', 'Book')
    author1 = Author.objects.create(name='Author 1')
    author2 = Author.objects.create(name='Author 2')
    Book.objects.create(title='Title 1.1', author=author1)
    Book.objects.create(title='Title 2.1', author=author1)
    Book.objects.create(title='Title 1.2', author=author2)
    Book.objects.create(title='Title 2.2', author=author2)


def backwards(apps, schema_editor):
    Author = apps.get_model('rename_app', 'Author')
    Author.objects.filter(name='Author 1').delete()
    Author.objects.filter(name='Author 2').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rename_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]