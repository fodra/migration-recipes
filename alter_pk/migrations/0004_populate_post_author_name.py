# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 08:36
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    Post = apps.get_model('alter_pk', 'Post')
    for post in Post.objects.select_related('author'):
        post.author_name = post.author.name
        post.save(update_fields=['author_name'])


def backwards(apps, schema_editor):
    Author = apps.get_model('alter_pk', 'Author')
    Post = apps.get_model('alter_pk', 'Post')
    authors = dict(Author.objects.values_list('name', 'pk'))
    for post in Post.objects.all():
        post.author_id = authors[post.author_name]
        post.save(update_fields=['author_id'])


class Migration(migrations.Migration):

    dependencies = [
        ('alter_pk', '0003_post_author_name'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
